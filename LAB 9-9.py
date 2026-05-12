class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __gt__(self, other):
        return self.x > other.y

    def __ge__(self, other):
        return self.x >= other.y

    def __lt__(self, other):
        return self.x < other.y

    def __le__(self, other):
        return self.x <= other.y

v1 = Vector(30, 40)
v2 = Vector(10, 20)

print(v1 > v2)
print(v1 >= v2)
print(v1 < v2)
print(v1 <= v2)
