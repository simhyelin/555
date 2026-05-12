import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, other):
        return self.magnitude() > other.magnitude()

    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def __le__(self, other):
        return self.magnitude() <= other.magnitude()

v1 = Vector(30, 40)
v2 = Vector(10, 20)

print(v1 > v2)
print(v1 >= v2)
print(v1 < v2)
print(v1 <= v2)
