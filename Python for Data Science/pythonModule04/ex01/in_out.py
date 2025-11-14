def square(x: int | float) -> int | float:
    """Return the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Return x raised to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Return a closure that applies function repeatedly on the result.
    
    Args:
        x: Initial value
        function: Function to apply (square or pow)
    
    Returns:
        A callable object (inner function) that applies the function
        on the previous result each time it's called
    """
    count = 0
    
    def inner() -> float:
        nonlocal count, x
        count += 1
        x = function(x)
        return x
    
    return inner
