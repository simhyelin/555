'''
class Rectangle:
    def __init__(self, side=0):
        self.side = side

    def getArea(self):
        return self.side*self.side
'''
'''
def printAreas(r, n):
    while n >= 1:
        print(r.side, "|t", r.getArea())
        r.side = r.side + 1
        n = n -1
'''
'''
r1 = Rectangle(10.0)
'''
'''
class Television:
    serialNumber = 0
    def __init__(self):
        Television.serialNumber += 1
        self.number = Television.serialNumber

t1= Television()
t2= Television()
myTv = Television()

print(t1.number, t2.number, myTv.number)
'''
class Television:
    serialNumber = 0
    def __init__(self):
        Television.serialNumber += 1
        self.number = Television.serialNumber

    def __str__(self):
        return'{}'.format(self.number)

t1= Television()
t2= Television()
myTv = Television()

print(t1, t2, myTv)

