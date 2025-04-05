import os
import re
import requests
import hashlib
import urllib.parse
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

    # 1. 标准Markdown格式: ![alt](url)
    md_pattern = r"!\[(.*?)\]\((https?://[^)]+)\)"
    for match in re.finditer(md_pattern, content):
        image_url = match.group(2)
        if image_url.startswith(("http://", "https://")):
            image_urls.append((image_url, "markdown", match.group(0)))

    # 2. HTML格式: <img src="url" ...>
    html_pattern = r"<img[^>]*src=[\"'](https?://[^\"']+)[\"'][^>]*>"
    for match in re.finditer(html_pattern, content):
        image_url = match.group(1)
        if image_url.startswith(("http://", "https://")):
            image_urls.append((image_url, "html", match.group(0)))

    # 3. 简易链接后缀
    link_pattern = (
        r"(?<!\!)\[(.*?)\]\((https?://[^)]+\.(jpg|jpeg|png|gif|webp|bmp|svg))\)"
    )
    for match in re.finditer(link_pattern, content):
        image_url = match.group(2)
        if image_url.startswith(("http://", "https://")):
            image_urls.append((image_url, "link", match.group(0)))

    return image_urls


def process_file(md_file, assets_dir, verbose=True, dry_run=False, subdir_depth=2):
    """处理单个Markdown文件"""
    try:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        # 提取所有图片URL
        image_entries = extract_image_urls(content)

        if not image_entries:
            if verbose:
                print(f"文件中没有找到外部图片链接: {md_file}")
            return 0, 0

        if verbose:
            print(f"处理文件: {md_file}, 找到 {len(image_entries)} 个图片链接")

        # 下载所有图片
        updates = []
        downloaded = 0
        failed = 0

        if dry_run:
            if verbose:
                print(f"[模拟执行] 将下载 {len(image_entries)} 张图片")
            return len(image_entries), 0

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_entry = {
                executor.submit(
                    download_image, url, assets_dir, 10, 3, verbose, subdir_depth
                ): (
                    url,
                    tag,
                    original,
                )
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
                    r"src=[\"']https?://[^\"']+[\"']",
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
        if updated_content != content:
            if not dry_run:
                with open(md_file, "w", encoding="utf-8") as f:
                    f.write(updated_content)
                if verbose:
                    print(f"已更新文件: {md_file}")
            else:
                if verbose:
                    print(f"[模拟执行] 将更新文件: {md_file}")
        else:
            if verbose:
                print(f"文件无需更新: {md_file}")

        return downloaded, failed

    except Exception as e:
        if verbose:
            print(f"处理文件 {md_file} 时出错: {str(e)}")
        return 0, 0


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
    args = parser.parse_args()

    docs_dir = args.dir
    assets_dir = args.assets if args.assets else os.path.join(docs_dir, "assets")
    verbose = not args.quiet
    dry_run = args.dry_run
    subdir_depth = args.depth

    if not os.path.exists(docs_dir):
        print(f"目录不存在: {docs_dir}")
        return

    if not dry_run:
        ensure_dir(assets_dir)

    # 如果只处理一个文件
    if args.file:
        if not os.path.exists(args.file):
            print(f"文件不存在: {args.file}")
            return
        downloaded, failed = process_file(
            args.file, assets_dir, verbose, dry_run, subdir_depth
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

    # 处理所有文件，显示进度条
    total_downloaded = 0
    total_failed = 0

    for md_file in tqdm(md_files, desc="处理Markdown文件", disable=not verbose):
        downloaded, failed = process_file(
            md_file, assets_dir, verbose, dry_run, subdir_depth
        )
        total_downloaded += downloaded
        total_failed += failed

    print(f"处理完成! 下载成功 {total_downloaded} 张图片，失败 {total_failed} 张图片")


if __name__ == "__main__":
    main()
