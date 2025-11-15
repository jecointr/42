#!/usr/bin/env python3
"""
Spider.py - programme pour télécharger toutes les images d'un site web
avec options récursives et gestion propre de Ctrl+C.
"""

import argparse
import os
import re
import requests
from urllib.parse import urljoin, urlparse

# Extensions autorisées pour le téléchargement
IMG_EXT = (".jpg", ".jpeg", ".png", ".gif", ".bmp")

# ------------------------------
# Gestion des arguments du programme
# ------------------------------
def parse_args():
    parser = argparse.ArgumentParser(description="Download all images from a website.")
    parser.add_argument("url", help="URL to explore")
    parser.add_argument("-r", action="store_true", help="Enable recursive download")
    parser.add_argument("-l", type=int, default=5, help="Max recursion depth (default: 5)")
    parser.add_argument("-p", default="./data/", help="Output folder (default: ./data/)")
    return parser.parse_args()

# ------------------------------
# Récupération du contenu HTML d'une page
# ------------------------------
def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/116.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.get(url, headers=headers, timeout=5)
        resp.raise_for_status()  # Vérifie que la requête a réussi
        return resp.text
    except Exception as e:
        print(f"[ERROR] Could not fetch {url}: {e}")
        return None

# ------------------------------
# Extraction des images et liens pour le crawl
# ------------------------------
def extract_links(html, base_url):
    # Regex pour extraire les images
    img_regex = r'<img[^>]+src="([^">]+)"'
    # Regex pour extraire les liens hypertextes
    link_regex = r'<a[^>]+href="([^">]+)"'
    imgs = [urljoin(base_url, src) for src in re.findall(img_regex, html)]
    links = [urljoin(base_url, href) for href in re.findall(link_regex, html)]
    return imgs, links

# ------------------------------
# Téléchargement d'une image
# ------------------------------
def download_image(url, out_dir):
    if not url.lower().endswith(IMG_EXT):
        return False  # Ignorer si ce n'est pas une extension autorisée
    os.makedirs(out_dir, exist_ok=True)
    filename = os.path.join(out_dir, os.path.basename(urlparse(url).path))
    try:
        resp = requests.get(url, timeout=5)
        with open(filename, "wb") as f:
            f.write(resp.content)
        print(f"[OK] {filename}")
        return True
    except KeyboardInterrupt:
        # Interruption volontaire par l'utilisateur
        raise  # Propagation de l'exception pour arrêter tout le programme
    except:
        print(f"[FAIL] {url}")
        return False

# ------------------------------
# Fonction récursive pour crawler les pages et télécharger les images
# ------------------------------
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
    # Télécharger toutes les images de cette page
    for img in imgs:
        download_image(img, out_dir)
    # Crawl récursif pour chaque lien trouvé
    for link in links:
        if link.startswith("http"):
            crawl(link, depth + 1, max_depth, out_dir, visited)

# ------------------------------
# Fonction principale
# ------------------------------
def main():
    args = parse_args()
    visited = set()
    try:
        if args.r:
            # Mode récursif
            crawl(args.url, 0, args.l, args.p, visited)
        else:
            # Mode non-récursif, juste la page donnée
            html = fetch_page(args.url)
            if html:
                imgs, _ = extract_links(html, args.url)
                if not imgs:
                    print("No images found at this URL.")
                for img in imgs:
                    download_image(img, args.p)
    except KeyboardInterrupt:
        # Arrêt propre en cas de Ctrl+C
        print("\n[INFO] Crawl interrupted by user. Images téléchargées jusqu'ici restent dans le dossier de sortie.")

# ------------------------------
# Point d'entrée du script
# ------------------------------
if __name__ == "__main__":
    main()

