def ft_filter(function, iterable):
    """Replacement for built-in filter()."""
    return [item for item in iterable if function(item)]
