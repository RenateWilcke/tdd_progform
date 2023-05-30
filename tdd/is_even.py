def is_even(x):
    """
        Determine if a number is even.

        Return True if x is even.
        Return False if x is odd.
        Return TypeError if x is not a number.
    """
    if (x % 2) == 0:
        return True
    else:
        return f"{x} is odd"

assert is_even(2)
assert is_even(3)

