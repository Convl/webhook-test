"""
Unit tests for the calculator module.
"""

import unittest
import calculator


class TestCalculator(unittest.TestCase):
    """Test cases for calculator operations."""

    def test_add(self):
        """Test addition operation."""
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(0, 0), 0)
        self.assertAlmostEqual(calculator.add(0.1, 0.2), 0.3, places=7)

    def test_subtract(self):
        """Test subtraction operation."""
        self.assertEqual(calculator.subtract(5, 3), 2)
        self.assertEqual(calculator.subtract(1, 1), 0)
        self.assertEqual(calculator.subtract(-1, -1), 0)
        self.assertEqual(calculator.subtract(10, 15), -5)

    def test_multiply(self):
        """Test multiplication operation."""
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 3), -6)
        self.assertEqual(calculator.multiply(0, 5), 0)
        self.assertEqual(calculator.multiply(-2, -3), 6)

    def test_divide(self):
        """Test division operation."""
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(7, 2), 3.5)
        self.assertEqual(calculator.divide(-6, 3), -2)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)

    def test_power(self):
        """Test power operation."""
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 0), 1)
        self.assertEqual(calculator.power(4, 0.5), 2)
        self.assertEqual(calculator.power(-2, 2), 4)

    def test_modulus(self):
        """Test modulus operation."""
        self.assertEqual(calculator.modulus(10, 3), 1)
        self.assertEqual(calculator.modulus(15, 4), 3)
        self.assertEqual(calculator.modulus(8, 2), 0)
        self.assertEqual(calculator.modulus(7, 7), 0)
        self.assertEqual(calculator.modulus(-10, 3), 2)  # Python's modulus behavior
        self.assertEqual(calculator.modulus(10, -3), -2)  # Python's modulus behavior
        self.assertAlmostEqual(calculator.modulus(5.5, 2), 1.5, places=10)

    def test_modulus_by_zero(self):
        """Test modulus by zero raises ValueError."""
        with self.assertRaises(ValueError):
            calculator.modulus(10, 0)
        with self.assertRaises(ValueError):
            calculator.modulus(-5, 0)

    def test_square_root(self):
        """Test square root operation."""
        self.assertEqual(calculator.square_root(4), 2)
        self.assertEqual(calculator.square_root(9), 3)
        self.assertEqual(calculator.square_root(0), 0)
        self.assertAlmostEqual(calculator.square_root(2), 1.4142135623730951, places=10)
        self.assertAlmostEqual(calculator.square_root(0.25), 0.5, places=10)

    def test_square_root_negative(self):
        """Test square root of negative number raises ValueError."""
        with self.assertRaises(ValueError):
            calculator.square_root(-1)
        with self.assertRaises(ValueError):
            calculator.square_root(-4)

    def test_factorial(self):
        """Test factorial operation."""
        self.assertEqual(calculator.factorial(0), 1)
        self.assertEqual(calculator.factorial(1), 1)
        self.assertEqual(calculator.factorial(2), 2)
        self.assertEqual(calculator.factorial(3), 6)
        self.assertEqual(calculator.factorial(4), 24)
        self.assertEqual(calculator.factorial(5), 120)
        self.assertEqual(calculator.factorial(10), 3628800)

    def test_factorial_negative(self):
        """Test factorial of negative number raises ValueError."""
        with self.assertRaises(ValueError):
            calculator.factorial(-1)
        with self.assertRaises(ValueError):
            calculator.factorial(-5)

    def test_factorial_non_integer(self):
        """Test factorial of non-integer raises ValueError."""
        with self.assertRaises(ValueError):
            calculator.factorial(3.5)
        with self.assertRaises(ValueError):
            calculator.factorial(2.1)

    def test_get_available_operations(self):
        """Test getting available operations."""
        operations = calculator.get_available_operations()
        expected = ["add", "subtract", "multiply", "divide", "power", "modulus", "square_root", "factorial"]
        self.assertEqual(operations, expected)


if __name__ == "__main__":
    unittest.main()
