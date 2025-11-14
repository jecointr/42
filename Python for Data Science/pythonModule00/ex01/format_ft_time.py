from datetime import datetime
from time import time


def main():
    now = time()
    print(f"Seconds since January 1, 1970: {now:,.4f} or {now:.2e} in scientific notation")
    print(datetime.now().strftime("%b %d %Y"))


if __name__ == "__main__":
    main()

