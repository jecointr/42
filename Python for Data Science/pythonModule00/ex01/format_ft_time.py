from time import time
from datetime import datetime


def main():
    now = time()
    msg = (
        f"Seconds since January 1, 1970: {now:,.4f} "
        f"or {now:.2e} in scientific notation"
    )
    print(msg)
    print(datetime.now().strftime("%b %d %Y"))
