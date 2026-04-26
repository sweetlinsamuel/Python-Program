#5)Create a Student class with public variable name and access and modify it directly from outside the class.

class Student:
    def __init__(self,name):
        self.name = name


s = Student("Priya")
print("student name:", s.name)

s.name = "Sita"
print("new student name:", s.name)
