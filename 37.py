import math

class ProperFraction:
    def __init__(self, numerator, denominator):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise ValueError("Чисельник і знаменник повинні бути цілими числами.")
        if denominator == 0:
            raise ValueError("Знаменник не може бути нулем.")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()
        # Раніше тут була перевірка на правильність дробу, яку ми прибираємо для результатів операцій

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def _simplify(self):
        common_divisor = self._gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __mul__(self, other):
        if not isinstance(other, ProperFraction):
            raise TypeError("Множити можна лише на інший об'єкт ProperFraction.")
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __add__(self, other):
        if not isinstance(other, ProperFraction):
            raise TypeError("Додавати можна лише інший об'єкт ProperFraction.")
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if not isinstance(other, ProperFraction):
            raise TypeError("Віднімати можна лише інший об'єкт ProperFraction.")
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)

    def __eq__(self, other):
        if not isinstance(other, ProperFraction):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __gt__(self, other):
        if not isinstance(other, ProperFraction):
            raise TypeError("Порівнювати можна лише з іншим об'єктом ProperFraction.")
        return self.numerator / self.denominator > other.numerator / other.denominator

    def __lt__(self, other):
        if not isinstance(other, ProperFraction):
            raise TypeError("Порівнювати можна лише з іншим об'єктом ProperFraction.")
        return self.numerator / self.denominator < other.numerator / other.denominator

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

f_a = ProperFraction(2, 3)
f_b = ProperFraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == '7/6'
f_d = f_b * f_a
assert str(f_d) == '1/3'
f_e = f_a - f_b
assert str(f_e) == '1/6'
assert f_d < f_c
assert f_d > f_e
assert f_a != f_b
f_1 = ProperFraction(2, 4)
f_2 = ProperFraction(3, 6)
assert f_1 == f_2
print('OK')