"""Perform mathematical calculations.

This module provides functions for basic mathematical operations such as addition, subtraction, multiplication, and division.

Module Usage Examples:
    >>> from calculator import add
    >>> add(2, 4)
    6.0
    >>> from calculator import multiply
    >>> multiply(2.0, 4.0)
    8.0
    >>> from calculator import divide
    >>> divide(4.0, 2)
    2.0

Function Details:
    - add(a, b): Compute and return the sum of two numbers.
    - subtract(a, b): Compute and return the difference between two numbers.
    - multiply(a, b): Compute and return the product of two numbers.
    - divide(a, b): Compute and return the quotient of two numbers.

Note:
    - The functions in this module handle both float and integer inputs.
"""

from typing import Union

def add(a: Union[float, int], b: Union[float, int]) -> float:
    """
    Compute and return the sum of two numbers.

    Args:
        a: A number representing the first addend in the addition.
        b: A number representing the second addend in the addition.

    Returns:
        A number representing the arithmetic sum of `a` and `b`.
    """
    return float(a + b)


def subtract(a: Union[float, int], b: Union[float, int]) -> float:
    """
    Compute and return the difference between two numbers.

    Args:
        a: A number representing the minuend.
        b: A number representing the subtrahend.

    Returns:
        A number representing the result of subtracting `b` from `a`.
    """
    return float(a - b)


def multiply(a: Union[float, int], b: Union[float, int]) -> float:
    """
    Compute and return the product of two numbers.

    Args:
        a: A number representing the multiplicand.
        b: A number representing the multiplier.

    Returns:
        A number representing the result of multiplying `a` by `b`.
    """
    return float(a * b)

def divide(a: float, b: float) -> float:
    """
    Compute and return the quotient of two numbers.

    Args:
        a: A number representing the dividend.
        b: A number representing the divisor.

    Returns:
        A number representing the result of dividing `a` by `b`.

    Raises:
        ZeroDivisionError: If `b` is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
