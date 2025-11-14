def count_in_list(lst, value):
    """Return number of occurrences of value in lst."""
    return sum(1 for x in lst if x == value)
