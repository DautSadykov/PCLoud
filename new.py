class Fraction:
    def __init__(self, n, d=None):
        if d is None:
            n, d = n.split('/')
        self.num = int(n)
        self.denom = int(d)
        self._simplify()

    def _gcd(self, a, b):
        """Helper function to compute the greatest common divisor of two integers."""
        while b:
            a, b = b, a % b
        return a

    def _simplify(self):
        """Helper function to simplify the fraction by dividing the numerator and denominator by their GCD."""
        gcd = self._gcd(self.num, self.denom)
        self.num //= gcd
        self.denom //= gcd

    def __repr__(self):
        return f'Fraction(\'{self.__str__()}\')'

    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        else:
            return f'{self.num}/{self.denom}'

    def numerator(self, new_num=None):
        if new_num is not None:
            self.num = new_num
            self._simplify()
        else:
            return self.num

    def denominator(self, new_denom=None):
        if new_denom is not None:
            self.denom = new_denom
            self._simplify()
        else:
            return self.denom

    def __neg__(self):
        """Implements the unary minus operator for fractions."""
        return Fraction(-self.num, self.denom)



a = Fraction(1, 3)
b = Fraction(-2, 6)
c = Fraction(-3, 9)
d = Fraction(4, -12)
print(a, b, c, d)
print(*map(repr, (a, b, c, d)))
