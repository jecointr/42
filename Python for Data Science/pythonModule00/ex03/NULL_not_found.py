def NULL_not_found(object: any) -> int:
    """
    Prints the type of different “Null-like” values.
    Returns 0 on success and 1 on error.
    """
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    if isinstance(object, float) and object != object:  # NaN check
        print(f"Cheese: {object} {type(object)}")
        return 0
    if object == 0 and type(object) is int:
        print(f"Zero: {object} {type(object)}")
        return 0
    if object == "" and type(object) is str:
        print(f"Empty: {type(object)}")
        return 0
    if object is False:
        print(f"Fake: {object} {type(object)}")
        return 0

    print("Type not Found")
    return 1


def main():
    pass


if __name__ == "__main__":
    main()
