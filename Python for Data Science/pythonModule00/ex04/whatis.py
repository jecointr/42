import sys

def main():
    args = sys.argv[1:]

    try:
        if len(args) == 0:
            return  # Pas d'argument, rien à faire

        if len(args) > 1:
            raise AssertionError("more than one argument is provided")

        try:
            n = int(args[0])
        except ValueError:
            raise AssertionError("argument is not an integer")

        if n % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()

