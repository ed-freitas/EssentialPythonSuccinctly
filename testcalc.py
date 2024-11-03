import unittest
from calc import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up a Calculator instance before each test method."""
        self.calc = Calculator()

    def test_add(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)

    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertRaises(ValueError, self.calc.divide, 10, 0)

if __name__ == "__main__":
    unittest.main()
