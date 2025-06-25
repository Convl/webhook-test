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

    def test_get_available_operations(self):
        """Test getting available operations."""
        operations = calculator.get_available_operations()
        expected = ["add", "subtract", "multiply", "divide", "power"]
        self.assertEqual(operations, expected)


if __name__ == "__main__":
    unittest.main()
