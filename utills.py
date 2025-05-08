""" Moduł zawiera funkcje pomocnicze """

# przykladowe funkcje utils .py
def add ( a: int , b: int) -> int:
    """
    Adds two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """
    return a + b

def subtract ( a: int , b: int) -> int:
    """
    Subtracts the second integer from the first.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The result of a - b.
    """
    return a - b

def multiply ( a: int , b: int) -> int:
    """
    Multiplies two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of a and b.
    """
    return a * b

def divide ( a: int , b: int) -> float :
    """
    Divides the first integer by the second.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of a / b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    return a / b
