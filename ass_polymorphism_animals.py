#2) Create a Parent class Animal with sound() method and override it in Dog and Cat classes with different outputs.

class Animal:
    def sound(self):
        print("Sounds of animal")


class Dog(Animal):
    def sound(self):
        print("Dogs bark")


class Cat(Animal):
    def sound(self):
        print("Cats meows")

a=Animal()
d=Dog()
c=Cat()

a.sound()
d.sound()
c.sound()

