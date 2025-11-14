import sys
import string


def count_chars(text: str) -> dict:
    """Return count dictionary of text categories."""
    return {
        "upper": sum(c.isupper() for c in text),
        "lower": sum(c.islower() for c in text),
        "punct": sum(c in string.punctuation for c in text),
        "spaces": sum(c.isspace() for c in text),
        "digits": sum(c.isdigit() for c in text),
    }


def main():
    """
    Count characters from argv or input()
    Simulate carriage return as space.
    """
    try:
        args = sys.argv[1:]

        if len(args) > 1:
            raise AssertionError("more than one argument is provided")

        if len(args) == 0:
            print("What is the text to count?")
            try:
                text = input()
                text += " "  # simuler le retour chariot comme un espace
            except EOFError:
                return
        else:
            text = args[0]

        counts = count_chars(text)
        print(f"The text contains {len(text)} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punct']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
