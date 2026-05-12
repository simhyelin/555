'''
class Car :
    name = ""
    speed = 0

    def __init__(self, name, speed) :
        self.name = name
        self.speed = speed

    def getName(self) :
        return self.name

    def getSpeed(self) :
        return self.speed

car1, car2 = None, None

car1 = car("아우디", 0)
car2 = car("벤츠", 30)

print("%s의 현재 속도는 %d입니다." % (car1.getName(), car1.getSpeed()))
print("%s의 현재 속도는 %d입니다." % (car2.getName(), car2.getSpeed()))

'''
class Car :
    def __init__(self, name="", speed=0) :
        self.name = name
        self.speed = speed

    def getName(self) :
        return self.name

    def getSpeed(self) :
        return self.speed

    def speedUp(self, value):
        self.speed += value

    def speedDown(self, value):
        self.speed -= value

    def __str__(self):
        return '{}의 속도는 {}입니다.'.format(self.name, self.speed)
'''
car1 = Car()
car2 = Car("벤츠", 30)
car1.speedUp(40)
car2.speedUp(10)
car2.speedDown(30)
print(car1, car2)
'''
class Sedan(Car): #위에서 코딩한 Car를 상속받았다.
    def speedUp(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150

    def speedDown(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0

myCar = Sedan("K5", 50)
print(myCar)
