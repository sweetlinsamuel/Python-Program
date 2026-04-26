#Create a Calculator class with a add() method that works for 2 numbers and 3 numbers using default arguments.


class Calculator:
    def add(self,a,b, c=0):
        return a+b+c

c = Calculator()
print("add two numbers:",c.add(2,3))
print("add two numbers:",c.add(2,3,4))

