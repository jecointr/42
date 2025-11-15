from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate various statistics based on the provided arguments.

    Args:
        *args: Variable number of numeric values
        **kwargs: Statistical measures to calculate
            (mean, median, quartile, std, var)
    """
    # Check if we have any data
    if not args:
        for _ in kwargs:
            print("ERROR")
        return

    # Convert args to a sorted list for calculations
    data = sorted(args)
    n = len(data)

    # Process each requested statistic
    for key, value in kwargs.items():
        if value == "mean":
            mean = sum(data) / n
            print(f"mean : {mean}")

        elif value == "median":
            if n % 2 == 0:
                median = (data[n // 2 - 1] + data[n // 2]) / 2
            else:
                median = data[n // 2]
            print(f"median : {median}")

        elif value == "quartile":
            # Calculate Q1 (25th percentile) and Q3 (75th percentile)
            def calculate_quartile(data, percentile):
                index = (len(data) - 1) * percentile
                lower = int(index)
                upper = lower + 1
                weight = index - lower

                if upper >= len(data):
                    return float(data[lower])
                return data[lower] * (1 - weight) + data[upper] * weight

            q1 = calculate_quartile(data, 0.25)
            q3 = calculate_quartile(data, 0.75)
            print(f"quartile : [{q1}, {q3}]")

        elif value == "std":
            # Standard deviation
            mean = sum(data) / n
            variance = sum((x - mean) ** 2 for x in data) / n
            std = variance ** 0.5
            print(f"std : {std}")

        elif value == "var":
            # Variance
            mean = sum(data) / n
            variance = sum((x - mean) ** 2 for x in data) / n
            print(f"var : {variance}")
