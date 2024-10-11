import os
import requests
import json
from pathlib import Path

NOTION_TOKEN = os.environ['NOTION_TOKEN']
NOTION_DATABASE_ID = os.environ['NOTION_DATABASE_ID']
CHANGED_FILES = os.environ['CHANGED_FILES'].split()

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def get_page_id(title):
    url = f"https://api.notion.com/v1/databases/{NOTION_DATABASE_ID}/query"
    payload = {
        "filter": {
            "property": "title",
            "title": {
                "equals": title
            }
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    results = response.json().get('results', [])
    return results[0]['id'] if results else None

def create_or_update_notion_page(title, content):
    page_id = get_page_id(title)
    
    if page_id:
        url = f"https://api.notion.com/v1/pages/{page_id}"
        method = requests.patch
    else:
        url = "https://api.notion.com/v1/pages"
        method = requests.post

    payload = {
        "parent": { "database_id": NOTION_DATABASE_ID },
        "properties": {
            "title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            }
        },
        "children": [
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": content
                            }
                        }
                    ]
                }
            }
        ]
    }

    response = method(url, headers=headers, json=payload)
    return response.json()

def main():
    for file_path in CHANGED_FILES:
        if file_path.endswith('.md'):
            title = Path(file_path).stem
            content = read_markdown_file(file_path)
            response = create_or_update_notion_page(title, content)
            print(f"Synced {file_path} to Notion. Response: {response}")

if __name__ == "__main__":
    main()
