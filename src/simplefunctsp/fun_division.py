
def superdivide(a: float, b: float) -> float:
    """Add two numbers together.

    This function is documented in a way that mkdocstrings can
    automatically extract and render.

    Args:
      a: float The first number to in the numerator.
      b: float The second number to denominator.

    Returns:
      float The sum of ``a`` and ``b``.

    Examples:
        >>> superdivide(2, 3)
        1/3
        >>> superdivie(-1.5, 0.5)
        -1.5
    """
    return (a / b) / 2

def divide(a: float, b: float) -> float:
    """Add two numbers together.

    Does simple division.

    Args:
      a: float The first number in the numerator.
      b: float The second number in the denominator.

    Returns:
      float The division of ``a`` divided ``b``.

    Examples:
        >>> divide(4, 2)
        2
        >>> divide(5, 1)
        5
    """
    return a / b

# %%
