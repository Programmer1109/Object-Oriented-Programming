""" Object Oriented Programming(Tutorial 4)
There are two types of methods in object oriented programming is concerned. They are as follows:
        1. Instance method :- These methods are the most widely used methods. All methods we have used untill now are
    instance methods. These methods work with instance variables and hence, whilst declaring any instance method we have
    to make use of the 'self' keyword. For e.g, the '__init__' and 'average' methods used in our demo program are
    instance methods.
        2. Class method :- These methods are used with class variables. Whilst defining any class methods we firstly
    make use of the'cls' keyword and also exclusive define over the function definition the decorator '@classmethod'.
    In our program, the method 'getSchool' is a class variable as it uses the class variable and 'cls' keyword is sent as
    the default argument.
        3. Static method :- These methods are the ones which have got nothing to do either with a class variable or any
    instance variables. Neither do these methods use the 'self' keyword nor the 'cls' keyword. A static method comes in
    handy whenever you want to create a method that operates on a other objects besides the object accessing it.
    However, for defining a static method we do have to mention the decorator '@staticmethod' above the line where we
    have defined our static method. For e.g, the method 'getClass' in the program bellow are Static methods.

The key takeaway from these three methods is that in order to successfully define a method of any type we first need
to determine on what type of variables exactly should the method work. If the method was to work with class
variables then, mostly a class method is defined. If the method was to work with instance variables then, mostly a
instance method is defined.
Member functions of a class or Methods are also classified as:
        1. Accessor/Getter Methods :- These methods are used for only accessing the data i.e fetching certain data from
    the method. Here, the data is only read from the function and not written to the function. In our program, the
    getter/accessor method is 'average'.
        2. Mutator/Setter methods :- These methods are used exclusively for setting the data for an object. Here, the
    data is only written to the function and not retrieved from the function. The '__init__' method used in our example
    is used as a setter/mutator method wherein only setting the data takes place.
"""


class Student:
    school = 'Stanford'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def display(self):
        print("Marks in subject 1= ", self.m1)
        print("Marks in subject 2= ", self.m2)
        print("Marks in subject 2= ", self.m2)

    def average(self):
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls):
        print("School Name :- " + Student.school)

    @staticmethod
    def getClass(value):
        print("Class Name:- " + value)


student1 = Student(92, 76, 81)
student2 = Student(76, 84, 68)

student1.display()
student2.display()

print(student1.average())
print(student2.average())

print(student1.getSchool())
print(student2.getSchool())
print(student1.getClass('Physics'))
print(student2.getClass('Mathematics'))
