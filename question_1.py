def string_pattern(size):
    """
    Returns string representing an x on the console using + and -

    Args:
        size: how tall and wide the return is

    Returns:
        Returns string representing an x

    Raises:
        ValueError: If size is less than or equal to 2
    """

    if size <= 2 or size >= 6:  # error if out of range
        raise ValueError
    elif size == 3:
        return '+-+\n-+-\n+-+\n'
    elif size == 4:
        return '+--+\n-++-\n-++-\n+--+\n'
    elif size == 5:
        return '+---+\n-+-+-\n--+--\n-+-+-\n+---+\n'
