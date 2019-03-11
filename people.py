class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return ("Hi, my name is {}".format(self.name))

class Student(Person):
        def learn(self):
         return ("I get it!")

class Instructor(Person):
    def teach(self):
        return ("An object is an instance of a class")

nadia = Instructor("Nadia")
print(nadia.greet())

chris = Student("Chris")
print(chris.greet())         
