class Animal:
    def sound(self):
        return "some generic sound"


class Dog(Animal):
    def sound(self):
        return "bark"


class Cat(Animal):
    def sound(self):
        pass


animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())