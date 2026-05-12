class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Dog(name = '+self.name+')'
my_dog = Dog('Jindo')
print(my_dog)
