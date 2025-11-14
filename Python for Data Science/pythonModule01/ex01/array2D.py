from typing import List, Union

Number = Union[int, float]

def slice_me(family: List[List[Number]], start: int, end: int) -> List[List[Number]]:
    """
    Slice a 2D array (list of lists) from start to end index.
    
    :param family: 2D list
    :param start: starting index (inclusive)
    :param end: ending index (exclusive)
    :return: truncated 2D list
    :raises ValueError: if input is not a 2D list or rows have different lengths
    """
    if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
        raise ValueError("Input must be a 2D list.")
    
    if len(family) == 0:
        return []
    
    row_length = len(family[0])
    if not all(len(row) == row_length for row in family):
        raise ValueError("All rows must have the same length.")
    
    print(f"My shape is : ({len(family)}, {row_length})")
    
    # Slicing
    truncated = family[start:end]
    
    new_shape = (len(truncated), row_length)
    print(f"My new shape is : {new_shape}")
    
    return truncated

def main():
    try:
        family = [
            [1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]
        ]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
