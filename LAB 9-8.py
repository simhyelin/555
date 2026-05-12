class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

v1 = Vector(30, 40)
v2 = Vector(10, 20)
v3 = v1 * v2
print('v1 * v2 =', v3)
v4 = v1 / v2
print('v1 / v2 =', v4)

v1 = Vector(10, 20)
print('-v1 =', -v1)    
