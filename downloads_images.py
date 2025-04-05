import os
import re
import requests
import hashlib
import urllib.parse
import json
from pathlib import Path
from urllib.parse import urlparse, unquote
import concurrent.futures
import time
import sys
import argparse
from tqdm import tqdm


def ensure_dir(directory):
    """确保目录存在，如果不存在则创建"""
    os.makedirs(directory, exist_ok=True)


def get_image_extension(url, content_type=None):
    """尝试获取图片扩展名"""
    # 首先尝试从URL中获取
    parsed_url = urlparse(url)
    path = unquote(parsed_url.path)
    if "." in path:
        ext = os.path.splitext(path)[1].lower()
        if ext in [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"]:
            return ext

    # 从Content-Type获取
    if content_type:
        if "jpeg" in content_type or "jpg" in content_type:
            return ".jpg"
        elif "png" in content_type:
            return ".png"
        elif "gif" in content_type:
            return ".gif"
        elif "webp" in content_type:
            return ".webp"
        elif "svg" in content_type:
            return ".svg"
        elif "bmp" in content_type:
            return ".bmp"

    # 默认返回jpg
    return ".jpg"


def get_subdirectory_for_hash(url_hash, depth=2):
    """根据哈希值创建子目录路径

    Args:
        url_hash: 文件URL的哈希值
        depth: 目录深度，取哈希值前多少位作为子目录

    Returns:
        子目录路径，如 "a/b" 表示取哈希值前2位
    """
    return os.path.join(*list(url_hash[:depth]))


def download_image(
    url, base_assets_dir, timeout=10, retries=3, verbose=True, subdir_depth=2
):
    """下载图片并返回保存路径，支持重试"""
    original_url = url

    # 处理微信图片URL特殊格式
    if "&amp;" in url:
        url = url.replace("&amp;", "&")

    for attempt in range(retries):
        try:
            # 使用MD5哈希值作为文件名，避免重复
            url_hash = hashlib.md5(original_url.encode()).hexdigest()

            # 创建子目录
            subdir = get_subdirectory_for_hash(url_hash, subdir_depth)
            save_dir = os.path.join(base_assets_dir, subdir)
            ensure_dir(save_dir)

            # 检查图片是否已经存在
            filename = f"{url_hash}{get_image_extension(url)}"
            save_path = os.path.join(save_dir, filename)

            if os.path.exists(save_path):
                if verbose:
                    print(f"图片已存在: {url} -> {save_path}")
                return os.path.join(subdir, filename)

            # 发送请求获取图片
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(url, timeout=timeout, headers=headers)
            if response.status_code != 200:
                if verbose:
                    print(
                        f"下载失败 {url}, 状态码: {response.status_code}, 尝试 {attempt+1}/{retries}"
                    )
                if attempt == retries - 1:
                    return None
                time.sleep(1)  # 等待1秒后重试
                continue

            # 获取文件扩展名
            content_type = response.headers.get("Content-Type", "")
            ext = get_image_extension(url, content_type)

            # 保存图片
            filename = f"{url_hash}{ext}"
            save_path = os.path.join(save_dir, filename)

            with open(save_path, "wb") as f:
                f.write(response.content)

            if verbose:
                print(f"已下载: {url} -> {save_path}")
            return os.path.join(subdir, filename)
        except Exception as e:
            if verbose:
                print(f"下载失败 {url}: {str(e)}, 尝试 {attempt+1}/{retries}")
            if attempt == retries - 1:
                return None
            time.sleep(1)  # 等待1秒后重试

    return None


def extract_image_urls(content):
    """提取内容中的所有图片URL"""
    image_urls = []
    local_images = []

    # 1. 标准Markdown格式: ![alt](url)，外部链接
    md_pattern = r"!\[(.*?)\]\((https?://[^)]+)\)"
    for match in re.finditer(md_pattern, content):
        image_url = match.group(2)
        if image_url.startswith(("http://", "https://")):
            image_urls.append((image_url, "markdown", match.group(0)))

    # 2. HTML格式: <img src="url" ...>，外部链接
    html_pattern = r'<img[^>]*src=["\'](https?://[^"\']+)["\'][^>]*>'
    for match in re.finditer(html_pattern, content):
        image_url = match.group(1)
        if image_url.startswith(("http://", "https://")):
            image_urls.append((image_url, "html", match.group(0)))

    # 3. 简易链接后缀，外部链接
    link_pattern = (
        r"(?<!\!)\[(.*?)\]\((https?://[^)]+\.(jpg|jpeg|png|gif|webp|bmp|svg))\)"
    )
    for match in re.finditer(link_pattern, content):
        image_url = match.group(2)
        if image_url.startswith(("http://", "https://")):
            image_urls.append((image_url, "link", match.group(0)))

    # 4. 标准Markdown格式: ![alt](assets/path/to/image.ext)，本地链接
    local_md_pattern = r"!\[(.*?)\]\((assets/[^)]+)\)"
    for match in re.finditer(local_md_pattern, content):
        local_path = match.group(2)
        local_images.append(local_path)

    # 5. HTML格式: <img src="assets/path/to/image.ext" ...>，本地链接
    local_html_pattern = r'<img[^>]*src=["\'](assets/[^"\']+)["\'][^>]*>'
    for match in re.finditer(local_html_pattern, content):
        local_path = match.group(1)
        local_images.append(local_path)

    return image_urls, local_images


def load_processed_files(index_file):
    """加载已处理过的文件索引"""
    if not os.path.exists(index_file):
        return {}

    try:
        with open(index_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"加载索引文件失败: {str(e)}")
        return {}


def save_processed_file(index_file, file_path, file_info):
    """保存处理过的文件信息到索引"""
    try:
        processed_files = load_processed_files(index_file)
        processed_files[file_path] = file_info

        with open(index_file, "w", encoding="utf-8") as f:
            json.dump(processed_files, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"保存索引文件失败: {str(e)}")


def is_file_modified(file_path, processed_files):
    """检查文件是否被修改过（根据修改时间和文件大小）"""
    if file_path not in processed_files:
        return True

    file_stat = os.stat(file_path)
    file_info = processed_files[file_path]

    # 检查修改时间和文件大小
    return file_stat.st_mtime != file_info.get(
        "mtime", 0
    ) or file_stat.st_size != file_info.get("size", 0)


def process_file(
    md_file,
    assets_dir,
    index_file,
    processed_files,
    verbose=True,
    dry_run=False,
    subdir_depth=2,
    force=False,
):
    """处理单个Markdown文件"""
    try:
        # 检查文件是否已处理且未修改
        if (
            not force
            and md_file in processed_files
            and not is_file_modified(md_file, processed_files)
        ):
            if verbose:
                print(f"跳过未修改文件: {md_file}")
            return 0, 0, True

        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # 提取所有图片URL和本地图片路径
        image_entries, local_images = extract_image_urls(content)

        if not image_entries and len(local_images) > 0:
            if verbose:
                print(
                    f"文件中没有找到外部图片链接，已有 {len(local_images)} 个本地图片: {md_file}"
                )

            # 记录处理信息
            if not dry_run:
                file_stat = os.stat(md_file)
                file_info = {
                    "mtime": file_stat.st_mtime,
                    "size": file_stat.st_size,
                    "processed_at": time.time(),
                    "images_count": len(local_images),
                    "local_images": local_images,
                }
                save_processed_file(index_file, md_file, file_info)

            return 0, 0, True

        if not image_entries and not local_images:
            if verbose:
                print(f"文件中没有找到任何图片链接: {md_file}")

            # 记录处理信息
            if not dry_run:
                file_stat = os.stat(md_file)
                file_info = {
                    "mtime": file_stat.st_mtime,
                    "size": file_stat.st_size,
                    "processed_at": time.time(),
                    "images_count": 0,
                }
                save_processed_file(index_file, md_file, file_info)

            return 0, 0, True

        if verbose:
            print(
                f"处理文件: {md_file}, 找到 {len(image_entries)} 个外部图片链接, {len(local_images)} 个本地图片"
            )

        # 下载所有图片
        updates = []
        downloaded = 0
        failed = 0

        if dry_run:
            if verbose:
                print(f"[模拟执行] 将下载 {len(image_entries)} 张图片")
            return len(image_entries), 0, False

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_entry = {
                executor.submit(
                    download_image, url, assets_dir, 10, 3, verbose, subdir_depth
                ): (url, tag, original)
                for url, tag, original in image_entries
            }
            for future in concurrent.futures.as_completed(future_to_entry):
                url, tag, original = future_to_entry[future]
                try:
                    relative_path = future.result()
                    if relative_path:
                        updates.append((url, tag, original, relative_path))
                        downloaded += 1
                    else:
                        failed += 1
                except Exception as e:
                    if verbose:
                        print(f"处理URL {url} 时出错: {str(e)}")
                    failed += 1

        # 更新Markdown文件中的图片链接
        updated_content = content
        for url, tag, original, relative_path in updates:
            if tag == "markdown":
                # 对于Markdown格式 ![alt](url)
                alt_text = re.search(r"!\[(.*?)\]", original).group(1)
                replacement = f"![{alt_text}](assets/{relative_path})"
                updated_content = updated_content.replace(original, replacement)
            elif tag == "html":
                # 对于HTML格式 <img src="url" ...>
                img_tag = re.sub(
                    r'src=["\'](https?://[^"\']+)["\']',
                    f'src="assets/{relative_path}"',
                    original,
                )
                updated_content = updated_content.replace(original, img_tag)
            elif tag == "link":
                # 对于链接格式 [text](url)
                link_text = re.search(r"\[(.*?)\]", original).group(1)
                replacement = f"[{link_text}](assets/{relative_path})"
                updated_content = updated_content.replace(original, replacement)

        # 若内容有更新，写回文件
        file_updated = False
        if updated_content != content:
            if not dry_run:
                with open(md_file, "w", encoding="utf-8") as f:
                    f.write(updated_content)
                if verbose:
                    print(f"已更新文件: {md_file}")
                file_updated = True
            else:
                if verbose:
                    print(f"[模拟执行] 将更新文件: {md_file}")
        else:
            if verbose:
                print(f"文件无需更新: {md_file}")

        # 更新后重新获取本地图片信息
        if file_updated:
            _, local_images = extract_image_urls(updated_content)

        # 记录处理信息
        if not dry_run:
            file_stat = os.stat(md_file)
            file_info = {
                "mtime": file_stat.st_mtime,
                "size": file_stat.st_size,
                "processed_at": time.time(),
                "images_count": (
                    len(local_images)
                    if file_updated
                    else len(local_images) + downloaded
                ),
                "downloaded": downloaded,
                "failed": failed,
                "updated": file_updated,
                "local_images": local_images,
            }
            save_processed_file(index_file, md_file, file_info)

        return downloaded, failed, downloaded == 0 and failed == 0

    except Exception as e:
        if verbose:
            print(f"处理文件 {md_file} 时出错: {str(e)}")
        return 0, 0, False


def main():
    # 定义命令行参数
    parser = argparse.ArgumentParser(description="下载Markdown文件中引用的图片")
    parser.add_argument(
        "--dir", type=str, default="docs", help="指定要处理的目录 (默认: docs)"
    )
    parser.add_argument(
        "--assets", type=str, help="指定保存图片的目录 (默认: <dir>/assets)"
    )
    parser.add_argument("--file", type=str, help="指定要处理的单个文件 (可选)")
    parser.add_argument(
        "--dry-run", action="store_true", help="模拟执行，不实际下载或修改文件"
    )
    parser.add_argument("--quiet", action="store_true", help="安静模式，减少输出")
    parser.add_argument(
        "--depth", type=int, default=2, help="子目录深度，基于哈希值前N位 (默认: 2)"
    )
    parser.add_argument(
        "--force", action="store_true", help="强制处理所有文件，忽略索引记录"
    )
    parser.add_argument(
        "--index", type=str, help="指定索引文件路径 (默认: <dir>/.processed_files.json)"
    )
    parser.add_argument(
        "--index-all",
        action="store_true",
        help="将所有已处理的文件（包含本地图片的文件）添加到索引中，不下载任何图片",
    )
    args = parser.parse_args()

    docs_dir = args.dir
    assets_dir = args.assets if args.assets else os.path.join(docs_dir, "assets")
    index_file = (
        args.index if args.index else os.path.join(docs_dir, ".processed_files.json")
    )
    verbose = not args.quiet
    dry_run = args.dry_run
    subdir_depth = args.depth
    force = args.force
    index_all = args.index_all

    if not os.path.exists(docs_dir):
        print(f"目录不存在: {docs_dir}")
        return

    if not dry_run and not index_all:
        ensure_dir(assets_dir)

    # 加载已处理文件索引
    processed_files = load_processed_files(index_file)
    if verbose and not dry_run:
        print(f"已加载 {len(processed_files)} 条处理记录")

    # 如果只处理一个文件
    if args.file and not index_all:
        if not os.path.exists(args.file):
            print(f"文件不存在: {args.file}")
            return
        downloaded, failed, _ = process_file(
            args.file,
            assets_dir,
            index_file,
            processed_files,
            verbose,
            dry_run,
            subdir_depth,
            force,
        )
        print(f"总计：下载成功 {downloaded} 张图片，失败 {failed} 张图片")
        return

    # 遍历所有Markdown文件
    md_files = []
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))

    if verbose:
        print(f"找到 {len(md_files)} 个Markdown文件")

    # 索引所有已处理文件模式
    if index_all:
        print("正在索引所有已处理的Markdown文件...")
        total_indexed = 0
        total_with_images = 0

        for md_file in tqdm(md_files, desc="索引Markdown文件", disable=not verbose):
            try:
                # 如果文件已经在索引中且未被修改，则跳过
                if md_file in processed_files and not is_file_modified(
                    md_file, processed_files
                ):
                    continue

                with open(md_file, "r", encoding="utf-8") as f:
                    content = f.read()

                # 提取所有图片URL和本地图片路径
                _, local_images = extract_image_urls(content)

                if local_images:
                    total_with_images += 1
                    file_stat = os.stat(md_file)
                    file_info = {
                        "mtime": file_stat.st_mtime,
                        "size": file_stat.st_size,
                        "processed_at": time.time(),
                        "images_count": len(local_images),
                        "local_images": local_images,
                        "indexed_only": True,
                    }
                    save_processed_file(index_file, md_file, file_info)
                    total_indexed += 1
                    if verbose:
                        print(
                            f"已索引文件: {md_file}，包含 {len(local_images)} 个本地图片"
                        )
            except Exception as e:
                if verbose:
                    print(f"索引文件 {md_file} 时出错: {str(e)}")

        print(
            f"索引完成! 共找到 {total_with_images} 个包含本地图片的文件，已成功索引 {total_indexed} 个文件"
        )
        return

    # 处理所有文件，显示进度条
    total_downloaded = 0
    total_failed = 0
    total_skipped = 0
    total_processed = 0

    for md_file in tqdm(md_files, desc="处理Markdown文件", disable=not verbose):
        downloaded, failed, skipped = process_file(
            md_file,
            assets_dir,
            index_file,
            processed_files,
            verbose,
            dry_run,
            subdir_depth,
            force,
        )
        total_downloaded += downloaded
        total_failed += failed
        if skipped and downloaded == 0 and failed == 0:
            total_skipped += 1
        else:
            total_processed += 1

    print(
        f"处理完成! 处理文件 {total_processed} 个，跳过 {total_skipped} 个，下载成功 {total_downloaded} 张图片，失败 {total_failed} 张图片"
    )


if __name__ == "__main__":
    main()
