"""Unit tests for the calculator library."""

from pathlib import Path
from toy_pkg.calculus import (add, subtract,
                              multiply, divide)


class TestCalculator:
    """Calss implementing tests for calculator.py."""

    def test_addition(self):
        """Tests for addition."""
        assert 4 == add(2, 2)
        assert 16 == add(10, 6)
        assert 0 == add(10, -10)

    def test_subtraction(self):
        """Tests for substraction."""
        assert 2 == subtract(4, 2)
        assert 20 == subtract(10, -10)
        assert 0 == subtract(10, 10)

    def test_multiplication(self):
        """Tests for multiplication."""
        assert 100 == multiply(10, 10)

    def test_division(self):
        """Tests for division."""
        assert 10 == divide(100, 10)
        assert 10 == divide(1000, 100)
