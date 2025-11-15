# give_bmi.py
from typing import List, Union

Number = Union[int, float]


def give_bmi(height: List[Number], weight: List[Number]) -> List[float]:
    """
    Calculate BMI for each pair of height and weight.

    :param height: list of heights in meters
    :param weight: list of weights in kg
    :return: list of BMI values
    :raises ValueError: if input lists have different lengths
        or contain invalid types
    """
    if not isinstance(height, list) or not isinstance(weight, list):
        raise ValueError("Both height and weight must be lists.")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")

    bmi_list = []
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise ValueError(
                "All height and weight values must be int or float."
            )
        if h <= 0:
            raise ValueError("Height must be greater than 0.")
        bmi_list.append(w / (h ** 2))

    return bmi_list


def apply_limit(bmi: List[Number], limit: int) -> List[bool]:
    """
    Check which BMI values exceed the given limit.

    :param bmi: list of BMI values
    :param limit: integer threshold
    :return: list of booleans (True if BMI > limit)
    :raises ValueError: if bmi is not a list or contains invalid types
    """
    if not isinstance(bmi, list):
        raise ValueError("BMI must be a list.")

    result = []
    for value in bmi:
        if not isinstance(value, (int, float)):
            raise ValueError("All BMI values must be int or float.")
        result.append(value > limit)

    return result


def main():
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi_values = give_bmi(height, weight)
        print(bmi_values, type(bmi_values))
        print(apply_limit(bmi_values, 26))
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
