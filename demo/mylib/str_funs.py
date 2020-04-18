def reverse(s):
    """Reverses the given string
    Params:
    s is a string

    Returns:
    Returns reversed version of the given string
    """
    return s[::-1]


def alpha(s):
    return list(filter(str.isalpha, s))
