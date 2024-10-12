import os
import re
import requests
import json
from pathlib import Path
from markdown import markdown
from bs4 import BeautifulSoup


NOTION_TOKEN = os.environ["NOTION_TOKEN"]
NOTION_DATABASE_ID = os.environ["NOTION_DATABASE_ID"]
CHANGED_FILES = os.environ.get("CHANGED_FILES", "").split("\n")


headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}


def convert_markdown_to_notion_blocks(markdown_text):
    # Convert Markdown to HTML
    html = markdown(markdown_text, extensions=["fenced_code", "tables"])

    # Parse HTML
    soup = BeautifulSoup(html, "html.parser")

    blocks = []

    for element in soup.children:
        if element.name in ["h1", "h2", "h3"]:
            heading_type = f"heading_{element.name[1]}"
            blocks.append(
                {
                    "object": "block",
                    "type": heading_type,
                    heading_type: {
                        "rich_text": [
                            {"type": "text", "text": {"content": element.text.strip()}}
                        ]
                    },
                }
            )
        elif element.name == "p":
            blocks.append(create_paragraph_block(element))
        elif element.name == "ul":
            for li in element.find_all("li", recursive=False):
                blocks.append(
                    {
                        "object": "block",
                        "type": "bulleted_list_item",
                        "bulleted_list_item": {
                            "rich_text": [
                                {"type": "text", "text": {"content": li.text.strip()}}
                            ]
                        },
                    }
                )
        elif element.name == "ol":
            for li in element.find_all("li", recursive=False):
                blocks.append(
                    {
                        "object": "block",
                        "type": "numbered_list_item",
                        "numbered_list_item": {
                            "rich_text": [
                                {"type": "text", "text": {"content": li.text.strip()}}
                            ]
                        },
                    }
                )
        elif element.name == "blockquote":
            blocks.append(
                {
                    "object": "block",
                    "type": "quote",
                    "quote": {
                        "rich_text": [
                            {"type": "text", "text": {"content": element.text.strip()}}
                        ]
                    },
                }
            )
        elif element.name == "pre":
            code = element.find("code")
            language = (
                code.get("class", [""])[0].replace("language-", "")
                if code.get("class")
                else ""
            )
            blocks.append(
                {
                    "object": "block",
                    "type": "code",
                    "code": {
                        "rich_text": [
                            {"type": "text", "text": {"content": code.text.strip()}}
                        ],
                        "language": language,
                    },
                }
            )
        elif element.name == "hr":
            blocks.append({"object": "block", "type": "divider", "divider": {}})
        elif element.name == "table":
            blocks.append(create_table_block(element))

    return blocks


def create_paragraph_block(element):
    rich_text = []
    for child in element.children:
        if child.name == "a":
            rich_text.append(
                {
                    "type": "text",
                    "text": {
                        "content": child.text,
                        "link": {"url": child.get("href", "")},
                    },
                }
            )
        elif child.name == "strong":
            rich_text.append(
                {
                    "type": "text",
                    "text": {"content": child.text},
                    "annotations": {"bold": True},
                }
            )
        elif child.name == "em":
            rich_text.append(
                {
                    "type": "text",
                    "text": {"content": child.text},
                    "annotations": {"italic": True},
                }
            )
        elif child.name == "code":
            rich_text.append(
                {
                    "type": "text",
                    "text": {"content": child.text},
                    "annotations": {"code": True},
                }
            )
        elif child.name == "img":
            return {
                "object": "block",
                "type": "image",
                "image": {
                    "type": "external",
                    "external": {"url": child.get("src", "")},
                },
            }
        else:
            rich_text.append({"type": "text", "text": {"content": str(child)}})

    return {
        "object": "block",
        "type": "paragraph",
        "paragraph": {"rich_text": rich_text},
    }


def create_table_block(table):
    rows = table.find_all("tr")
    has_header = table.find("thead") is not None

    table_block = {
        "object": "block",
        "type": "table",
        "table": {
            "table_width": len(rows[0].find_all(["th", "td"])),
            "has_column_header": has_header,
            "has_row_header": False,
            "children": [],
        },
    }

    for row in rows:
        cells = row.find_all(["th", "td"])
        row_block = {
            "type": "table_row",
            "table_row": {
                "cells": [
                    [{"type": "text", "text": {"content": cell.text.strip()}}]
                    for cell in cells
                ]
            },
        }
        table_block["table"]["children"].append(row_block)

    return table_block


def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def get_page_id(title):
    url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
    payload = {"filter": {"property": "title", "title": {"equals": title}}}
    response = requests.post(url, headers=headers, json=payload)
    results = response.json().get("results", [])
    return results[0]["id"] if results else None


def create_or_update_notion_page(title, content):
    page_id = get_page_id(title)

    if page_id:
        url = f"https://api.notion.com/v1/pages/{page_id}"
        method = requests.patch
    else:
        url = "https://api.notion.com/v1/pages"
        method = requests.post

    notion_blocks = convert_markdown_to_notion_blocks(content)

    payload = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": {"Name": {"title": [{"text": {"content": title}}]}},
        "children": notion_blocks,
    }

    response = method(url, headers=headers, json=payload)
    return response.json()


def main():
    if not CHANGED_FILES:
        print("No changed files detected. Exiting.")
        return

    for file_path in CHANGED_FILES:
        if file_path.endswith(".md"):
            try:
                print(f"Sync {file_path}")
                title = Path(file_path).stem
                content = read_markdown_file(file_path)
                response = create_or_update_notion_page(title, content)
                print(f"Synced {file_path} to Notion. Response: {response}")
            except Exception as e:
                print(f"Error processing {file_path}: {str(e)}")


if __name__ == "__main__":
    main()
