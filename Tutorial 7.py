''' Object Oriented Programming (Tutorial 7)
    Polymorphism is defined as the ability of an interfaces or entities to take many forms.
    In object oriented programming there are 4 ways of polymorphism can take place:-
        1. Duck Typing :- Duck typing basically builds on the idea that if a bird walks like a duck, quacks like a duck
    swims like a duck then it is definitely a duck. Similarly, in duck typing if a class contains a specific method
    then, it doesn't matter which class the object belongs to. For e.g, in our program both 'Pycharm' and "myEditor'
    contain a method execute. Hence, it doesn't matter which of the two class object is passed to laptop as they both
    contain an execute method.
        2. Operator Overloading :- There are many builtin operators in python. These operators are used to implement
    various operations like addition, subtraction, multiplication and division. However, these operators cannot add or
    subtract two class objects or add an 'int' class variable with a 'string'. If in case a programmer wants to
    implement in any program then, python allows for operator overloading i.e the programmer can redefine an existing
    operator with the same name.
        3. Method Overloading :- Method overloading basically allows the programmer to define one method more than once
    inside the same class by either changing the number of arguments or the types of arguments. This concept is present
    in other object oriented programming languages like C++, Java, etc. Unfortunately, method overloading in not
    available in Python.
        4. Method Overriding :- Method overriding allows a sub class to inherit all the methods mentioned in its super
    class. Hence, the object of sub class can access all the methods present in its super class. Also, a sub class can
    redefine a method already present in its super class.
'''


# example of Duck typing
class Pycharm:

    def execute(self):
        print("Run time error")
        print("Compiler error\n")


class myEditor:

    def execute(self):
        print("Spell check")
        print("Convention check")
        print("Run time error")
        print("Compiler error")


class Laptop:

    def processor(self, ide):
        ide.execute()


obj1 = Pycharm()
obj2 = myEditor()

lap = Laptop()
lap.processor(obj1)
lap.processor(obj2)


# example of operator overloading
class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        stud = Student(m1, m2)
        return stud

    def __gt__(self, other):
        score1 = self.m1 + self.m2
        score2 = other.m1 + other.m2
        if score1 > score2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(57, 63)
s2 = Student(53, 72)
s3 = Student(43, 67)
print(s1)
print(s2)
print(s3)
s4 = s1 + s2
print(s4.m1)
print(s4.m2)
print(s4)

if s1 > s2:
    print("Student1 wins!!!")
else:
    print("Student2 wins!!!")

if s1 > s3:
    print("Student1 wins")
else:
    print("Student3 wins")


# example for Method overriding
class Parent:

    def phone(self):
        company = 'Nokia'
        print(company)


class ChildA(Parent):

    def phone(self):
        company = 'Oppo'
        print(company)


class ChildB(Parent):
    pass


daughter = ChildA()
son = ChildB()
# although both son and daughter are accessing the same method the o/p will be different as son is object of class
# ChildB  whilst the daughter is class ChildA
son.phone()
daughter.phone()
