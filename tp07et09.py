from math import gcd

class Fraction:
    """Class representing a fraction and operations on it.

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : den != 0
        POST : Fraction is initialized in its reduced form.
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        common_divisor = gcd(num, den)
        self._numerator = num // common_divisor
        self._denominator = den // common_divisor
        if self._denominator < 0:  # Ensure denominator is positive
            self._numerator = -self._numerator
            self._denominator = -self._denominator

    @property
    def numerator(self):
        """Get the numerator."""
        return self._numerator

    @property
    def denominator(self):
        """Get the denominator."""
        return self._denominator

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction.

        PRE : none
        POST : Returns a string representation of the fraction.
        """
        return f"{self.numerator}/{self.denominator}" if self.denominator != 1 else str(self.numerator)

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number.

        A mixed number is the sum of an integer and a proper fraction.

        PRE : none
        POST : Returns a string of the mixed number form (e.g., "2 1/3").
        """
        if abs(self.numerator) < self.denominator:
            return str(self)  # Already a proper fraction
        integer_part = int((abs(self.numerator) // abs(self.denominator))*(abs(self.numerator)/self.numerator))
        remainder = abs(self.numerator) % self.denominator
        if remainder == 0:
            return str(integer_part)
        return f"{integer_part} {remainder}/{self.denominator}"

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions.

         PRE : other is a Fraction
         POST : Returns a new Fraction representing the sum.
         """
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        """Overloading of the - operator for fractions.

        PRE : other is a Fraction
        POST : Returns a new Fraction representing the difference.
        """
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        """Overloading of the * operator for fractions.

        PRE : other is a Fraction
        POST : Returns a new Fraction representing the product.
        """
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        """Overloading of the / operator for fractions.

        PRE : other is a Fraction and other.numerator != 0
        POST : Returns a new Fraction representing the division.
        """
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __pow__(self, other):
        """Overloading of the ** operator for fractions.

        PRE : other is an integer
        POST : Returns a new Fraction raised to the given power.
        """
        if other >= 0:
            num = self.numerator ** other
            den = self.denominator ** other
        else:  # Negative power inverts fraction
            num = self.denominator ** abs(other)
            den = self.numerator ** abs(other)
        return Fraction(num, den)

    def __eq__(self, other):
        """Overloading of the == operator for fractions.

        PRE : other is a Fraction
        POST : Returns True if fractions are equal, False otherwise.
        """
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __float__(self):
        """Returns the decimal value of the fraction.

        PRE : None
        POST : Returns the floating-point representation of the fraction.
        """
        return self.numerator / self.denominator

    # ------------------ Properties checking  ------------------

    def is_zero(self):
        """Check if a fraction's value is 0.

        PRE : None
        POST : Returns True if fraction is zero, False otherwise.
        """
        return self.numerator == 0

    def is_integer(self):
        """Check if a fraction is an integer (e.g., 8/4, 3, 2/2).

        PRE : None
        POST : Returns True if fraction is an integer, False otherwise.
        """
        return self.numerator % self.denominator == 0

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1.

        PRE : None
        POST : Returns True if fraction is proper, False otherwise.
        """
        return abs(self.numerator) < self.denominator

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form.

        PRE : None
        POST : Returns True if fraction is a unit fraction, False otherwise.
        """
        return self.numerator == 1 and self.denominator != 1

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction.

        Two fractions are adjacent if the absolute value of the difference is a unit fraction.

        PRE : other is a Fraction
        POST : Returns True if fractions are adjacent, False otherwise.
        """
        diff = self - other
        return diff.numerator == 1 and abs(diff.denominator) > 1

