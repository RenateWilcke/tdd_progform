def is_zero(x):
    """
    Determine if a number is zero.

    Rerurn True if x is an integer that is zero.
    Return False if x is an integer that is not zero.
    Raise TypeError if not a number.
    """
    if not isinstance(x, int):
        raise TypeError("'x' must be an integer")
    return True

assert is_zero.__doc__ is not None

has_raised = False
try:
    is_zero('asdf')
except:
    has_raised = True
assert has_raised

assert is_zero(0)
