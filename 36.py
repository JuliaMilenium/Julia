import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.get_square() == other.get_square()

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        total_area = self.get_square() + other.get_square()
        side = math.sqrt(total_area)
        return Rectangle(round(side, 2), round(total_area / side, 2))

    def __mul__(self, n):
        if not isinstance(n, (int, float)):
            return NotImplemented
        new_area = self.get_square() * n
        side = math.sqrt(new_area)
        return Rectangle(round(side, 2), round(new_area / side, 2))

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height}, area={self.get_square()})'


# --- Перевірка ---
r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8, 'Test1'
assert r2.get_square() == 18, 'Test2'

r3 = r1 + r2
assert round(r3.get_square()) == 26, 'Test3'

r4 = r1 * 4
assert round(r4.get_square()) == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'

print("✅ Усі тести пройдено успішно!")
