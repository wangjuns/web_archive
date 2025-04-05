#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import datetime
import mkdocs_gen_files


def generate_index(docs_dir="docs"):
    """生成文档索引"""
    markdown_files = []

    # 遍历所有文档目录
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md") and file != "index.md":
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, docs_dir)
                title = os.path.splitext(os.path.basename(full_path))[0]
                # 获取文件修改时间
                mod_time = os.path.getmtime(full_path)
                mod_date = datetime.fromtimestamp(mod_time).strftime("%Y-%m-%d")

                markdown_files.append(
                    {"title": title, "path": rel_path, "mod_date": mod_date}
                )

    # 按修改日期排序，最新的在前
    markdown_files.sort(key=lambda x: x["mod_date"], reverse=True)

    # 生成索引文件内容
    content = f"""# 文档索引

本索引包含 {len(markdown_files)} 个文档文件，按最后修改日期排序。

"""

    for file_info in markdown_files:
        content += f"- [{file_info['title']}](./{file_info['path']})\n"

    # 添加生成时间
    content += f"\n\n*索引生成于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*"

    return content


with mkdocs_gen_files.open("index.md", "w") as f:
    print(generate_index(), file=f)
