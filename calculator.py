"""
Simple Calculator Module

This module provides basic arithmetic operations for a calculator application.
"""

import math


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def subtract(a, b):
    """Subtract b from a and return the result."""
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """Divide a by b and return the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b and return the result."""
    return a**b


def modulus(a, b):
    """Calculate the remainder of a divided by b."""
    if b == 0:
        raise ValueError("Cannot calculate modulus with zero divisor")
    return a % b


def square_root(a):
    """Calculate the square root of a number."""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)


def factorial(a):
    """Calculate the factorial of a number."""
    if a < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if not a.is_integer():
        raise ValueError("Factorial is only defined for integers")
    return math.factorial(int(a))


def get_available_operations():
    """Return a list of available operations."""
    return ["add", "subtract", "multiply", "divide", "power", "modulus", "square_root", "factorial"]
