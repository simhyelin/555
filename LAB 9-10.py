class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

r1 = Rect(100, 200)
print(r1.__dict__)
print(r1.__dict__['width'])

class Rect:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

r1 = Rect(100, 200)
print(r1.__dict__)
print(r1.__dict__['_Rect__width'])
    
