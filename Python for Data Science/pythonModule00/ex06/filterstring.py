import sys
from ft_filter import ft_filter


def main():
    """Filter words from string longer than N using custom ft_filter."""
    try:
        args = sys.argv[1:]
        if len(args) != 2:
            raise AssertionError("the arguments are bad")

        s, n = args[0], args[1]

        if not isinstance(s, str):
            raise AssertionError("the arguments are bad")

        try:
            n = int(n)
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = s.split(" ")
        result = ft_filter(lambda w: len(w) > n, words)
        print(result)

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
