from typing import Any


def callLimit(limit: int):
    """
    Decorator factory that limits the number of times a function can be called.

    Args:
        limit: Maximum number of times the function can be called

    Returns:
        A decorator that wraps the function with call limiting
    """
    count = 0

    def callLimiter(function):
        """
        Decorator that wraps the function.

        Args:
            function: The function to be limited

        Returns:
            Wrapped function with call limiting
        """
        def limit_function(*args: Any, **kwds: Any):
            """
            Wrapper function that checks call count before execution.
            """
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter
