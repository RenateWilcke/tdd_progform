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



def is_odd(x):
    """
        Determine if a number is odd.

        Return True if x is odd.
        Return False if x is even.
        Return TypeError if x is not a number.
    """
    try:
        a = is_even(x)
    except TypeError:
        return f"{x} is not a number."
    else:
        if not a:
            return True
        else:
            return f"{x} is even"
    
assert is_odd.__doc__ is not None
assert is_odd(1)
assert is_odd(2)
is_odd('asd')
