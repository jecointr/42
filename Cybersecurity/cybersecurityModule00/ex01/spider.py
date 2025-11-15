#!/usr/bin/env python3
import argparse
import os
import re
import requests
from urllib.parse import urljoin, urlparse

# Extensions autorisées
IMG_EXT = (".jpg", ".jpeg", ".png", ".gif", ".bmp")

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL to explore")
    parser.add_argument("-r", action="store_true", help="Recursive mode")
    parser.add_argument("-l", type=int, default=5, help="Max recursion depth")
    parser.add_argument("-p", default="./data/", help="Output folder")
    return parser.parse_args()

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " 
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/116.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"[ERROR] Could not fetch {url}: {e}")
        return None

def extract_links(html, base_url):
    # Extraire les images
    img_regex = r'<img[^>]+src="([^">]+)"'
    # Extraire les liens pour le crawl récursif
    link_regex = r'<a[^>]+href="([^">]+)"'
    imgs = [urljoin(base_url, src) for src in re.findall(img_regex, html)]
    links = [urljoin(base_url, href) for href in re.findall(link_regex, html)]
    return imgs, links

def download_image(url, out_dir):
    if not url.lower().endswith(IMG_EXT):
        return False
    os.makedirs(out_dir, exist_ok=True)
    filename = os.path.join(out_dir, os.path.basename(urlparse(url).path))
    try:
        resp = requests.get(url, timeout=5)
        with open(filename, "wb") as f:
            f.write(resp.content)
        print(f"[OK] {filename}")
        return True
    except:
        print(f"[FAIL] {url}")
        return False

def crawl(url, depth, max_depth, out_dir, visited):
    if depth > max_depth or url in visited:
        return
    visited.add(url)
    html = fetch_page(url)
    if not html:
        return
    imgs, links = extract_links(html, url)
    if not imgs and depth == 0:
        print("No images found at this URL.")
    for img in imgs:
        download_image(img, out_dir)
    for link in links:
        if link.startswith("http"):
            crawl(link, depth + 1, max_depth, out_dir, visited)

def main():
    args = parse_args()
    visited = set()
    if args.r:
        crawl(args.url, 0, args.l, args.p, visited)
    else:
        html = fetch_page(args.url)
        if html:
            imgs, _ = extract_links(html, args.url)
            if not imgs:
                print("No images found at this URL.")
            for img in imgs:
                download_image(img, args.p)

if __name__ == "__main__":
    main()

