import os
import sys


def ft_tqdm(lst: range):
    """
    Custom minimal tqdm-like progress bar using yield.
    """
    total = len(lst)
    try:
        width = os.get_terminal_size().columns - 20
    except OSError:
        width = 50  # fallback

    for i, elem in enumerate(lst, 1):
        progress = int((i / total) * width)
        bar = "[" + "=" * progress + ">" + " " * (width - progress) + "]"
        percent = int((i / total) * 100)
        sys.stdout.write(f"\r{percent:3d}%|{bar}| {i}/{total}")
        sys.stdout.flush()
        yield elem
    print()


def main():
    """Test ft_tqdm."""
    from time import sleep
    for _ in ft_tqdm(range(10)):
        sleep(0.1)


if __name__ == "__main__":
    main()
