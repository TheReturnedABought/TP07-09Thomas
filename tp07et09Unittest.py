from tp079 import Fraction
import unittest

class FractionTestCase(unittest.TestCase):

    # -------------------  Constructor -------------------

    def setUp(self):
        """Set up fractions for testing."""
        self.f1 = Fraction(3, 4)  # Normal fraction: 3/4
        self.f2 = Fraction(2, 1)  # Integer fraction: 2
        self.f3 = Fraction(-5, 2)  # Negative mixed fraction: -5/2
        self.f4 = Fraction(2, -4)  # Negative fraction: -1/2
        self.f_zero = Fraction(0, 1)  # Zero

    def test_constructor_invalid(self):
        """Test invalid fractions (denominator = 0)."""
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    # ------------------- Test String Representation -------------------

    def test_str(self):
        """Test string representation of fractions."""
        self.assertEqual(str(self.f1), "3/4")
        self.assertEqual(str(self.f2), "2")
        self.assertEqual(str(self.f3), "-5/2")
        self.assertEqual(str(self.f4), "-1/2")
        self.assertEqual(str(self.f_zero), "0")

    def test_as_mixed_number(self):
        """Test mixed number representation."""
        self.assertEqual(self.f1.as_mixed_number(), "3/4")
        self.assertEqual(self.f2.as_mixed_number(), "2")
        self.assertEqual(self.f3.as_mixed_number(), "-2 1/2")
        self.assertEqual(self.f4.as_mixed_number(), "-1/2")
        self.assertEqual(self.f_zero.as_mixed_number(), "0")

    # ------------------- Test Arithmetic Operations -------------------

    def test_addition(self):
        """Test addition of fractions."""
        self.assertEqual(self.f1 + self.f1, Fraction(3, 2))  # Normal fraction + normal
        self.assertEqual(self.f1 + self.f2, Fraction(11, 4))  # Normal + integer
        self.assertEqual(self.f1 + self.f3, Fraction(-7, 4))  # Normal + negative fraction1
        self.assertEqual(self.f1 + self.f4, Fraction(1, 4))  # Normal + negative fraction2
        self.assertEqual(self.f1 + self.f_zero, self.f1)  # Normal + zero

    def test_subtraction(self):
        """Test subtraction of fractions."""
        self.assertEqual(self.f2 - self.f1, Fraction(5, 4))  # Integer - normal
        self.assertEqual(self.f2 - self.f2, self.f_zero)  # Integer - integer
        self.assertEqual(self.f2 - self.f3, Fraction(9, 2))  # Integer - negative fraction1
        self.assertEqual(self.f2 - self.f4, Fraction(5, 2))  # Integer - negative fraction2
        self.assertEqual(self.f2 - self.f_zero, self.f2)  # Integer - zero

    def test_multiplication(self):
        """Test multiplication of fractions."""
        self.assertEqual(self.f3 * self.f1, Fraction(-15, 8)) # Negative fraction1  * normal
        self.assertEqual(self.f3 * self.f2, Fraction(-10, 2))  # Negative fraction1  * integer
        self.assertEqual(self.f3 * self.f3, Fraction(25, 4))  # Negative fraction1 * negative fraction1
        self.assertEqual(self.f3 * self.f4, Fraction(5, 4)) # Negative fraction1 * negative fraction2
        self.assertEqual(self.f3 * self.f_zero, self.f_zero) # Negative  * zero

    def test_division(self):
        """Test division of fractions."""
        self.assertEqual(self.f4 / self.f1, Fraction(-2, 3))  # Negative fraction ÷ normal
        self.assertEqual(self.f4 / self.f2, Fraction(-1, 4))  # Negative fraction2 ÷ integer
        self.assertEqual(self.f4 / self.f3, Fraction(1, 5))  # Negative fraction2 ÷ negative fraction1
        self.assertEqual(self.f4 / self.f4, Fraction(1, 1))  # Negative fraction2 ÷ negative fraction2
        with self.assertRaises(ZeroDivisionError):
            self.f4 / self.f_zero  # Division by zero

    def test_power(self):
        """Test exponentiation of fractions."""
        self.assertEqual(self.f1 ** 2, Fraction(9, 16))  # Normal fraction squared
        self.assertEqual(self.f2 ** 3, Fraction(8, 1))  # Integer fraction cubed
        self.assertEqual(self.f3 ** 2, Fraction(25, 4)) # Negative fraction1 squared
        self.assertEqual(self.f4 ** 3, Fraction(-1, 8))  # Negative fraction cubed
        self.assertEqual(self.f_zero ** 2, self.f_zero)  # Zero squared

    # ------------------- Test Comparison Operators -------------------

    def test_equality(self):
        """Test equality of fractions."""
        self.assertTrue(self.f1 == Fraction(6, 8))  # Equivalent normal fractions
        self.assertTrue(self.f2 == Fraction(4, 2))  # Equivalent integer fractions
        self.assertFalse(self.f3 == self.f1)  # Negative integer ≠ normal
        self.assertFalse(self.f4 == self.f3)  # Negative fraction ≠ negative fraction1
        self.assertTrue(self.f_zero == Fraction(0, 5))  # Equivalent zeros

    # ------------------- Test Conversion -------------------

    def test_float_conversion(self):
        """Test conversion to float."""
        self.assertAlmostEqual(float(self.f1), 0.75)  # Normal fraction
        self.assertAlmostEqual(float(self.f2), 2.0)  # Integer fraction
        self.assertAlmostEqual(float(self.f3), -2.5)  # Negative fraction1
        self.assertAlmostEqual(float(self.f4), -0.5)  # Negative fraction2
        self.assertAlmostEqual(float(self.f_zero), 0.0)  # Zero

    # ------------------- Test Fraction Properties -------------------

    def test_is_zero(self):
        """Test if a fraction is zero."""
        self.assertTrue(self.f_zero.is_zero())  # Zero
        self.assertFalse(self.f1.is_zero())  # Normal fraction
        self.assertFalse(self.f2.is_zero())  # Integer fraction
        self.assertFalse(self.f3.is_zero())  # Negative fraction1
        self.assertFalse(self.f4.is_zero())  # Negative fraction2

    def test_is_integer(self):
        """Test if a fraction is an integer."""
        self.assertFalse(self.f1.is_integer())  # Normal fraction
        self.assertTrue(self.f2.is_integer())  # Integer fraction
        self.assertFalse(self.f3.is_integer())  # Negative fraction1
        self.assertFalse(self.f4.is_integer())  # Negative fraction2
        self.assertTrue(self.f_zero.is_integer())  # Zero

    def test_is_proper(self):
        """Test if a fraction is proper."""
        self.assertTrue(self.f1.is_proper())  # Normal fraction
        self.assertFalse(self.f2.is_proper())  # Integer fraction
        self.assertFalse(self.f3.is_proper())  # Negative fraction1
        self.assertTrue(self.f4.is_proper())  # Negative fraction2
        self.assertTrue(self.f_zero.is_proper())  # Zero

    def test_is_unit(self):
        self.assertFalse(self.f1.is_unit())  # 3/4 is not a unit fraction
        self.assertFalse(self.f2.is_unit())  # 2 is not a unit fraction
        self.assertFalse(self.f3.is_unit())  # -5/2 is not a unit fraction
        self.assertFalse(self.f4.is_unit())
        self.assertFalse(self.f_zero.is_unit())
        self.assertTrue(Fraction(1, 2).is_unit())

    def test_is_adjacent_to(self):
        # Adjacent unit fraction differences
        self.assertFalse(self.f1.is_adjacent_to(self.f1))
        self.assertFalse(self.f2.is_adjacent_to(self.f2 ))
        self.assertFalse(self.f3.is_adjacent_to(self.f4))
        self.assertFalse(self.f4.is_adjacent_to(self.f1))
        self.assertTrue(Fraction(1,2).is_adjacent_to(Fraction(1,3)))

if __name__ == "__main__":
    # Run the tests
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
