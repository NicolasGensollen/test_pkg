"""Unit tests for the calculator library."""

from pathlib import Path
from toy_pkg import calculator


class TestCalculator:
    """Calss implementing tests for calculator.py."""

    def test_addition(self):
        """Tests for addition."""
        assert 4 == calculator.add(2, 2)
        assert 14 == calculator.add(10, 6)

    def test_subtraction(self):
        """Tests for substraction."""
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        """Tests for multiplication."""
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        """Tests for division."""
        assert 10 == calculator.divide(100, 10)
