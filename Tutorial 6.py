"""Object Oriented Programming(Tutorial 6)
    Inheritance can be defined as the process where one class acquires the properties (methods and fields) of another.
With the use of inheritance the information is made manageable in a hierarchical order.
    There are mainly three different ways of implementing inheritance in python. These are :-
        1. Single level inheritance :- In this type, we have a child/sub class which inherits all the methods and fields
    from the the parent/super class. In single level inheritance any sub class can have exactly one super class.
    For e.g, in the demo program the method 'game3' uses single level inheritance as it only inherits the methods of the
    one class i.e the class 'game1'.
        2. Multi level inheritance :- In this type, we have a child/sub class which inherits all the methods from its
    predecessors i.e methods contained by its super class and the methods its super class has inherited. For e.g, in the
     demo program the method 'game4' uses multi level inheritance as it inherits from game3 which again has inherited
     methods from game 1. Hence, according the the rules of inheritance in object oriented programming the class 'game4'
     implicitly inherits methods from the class 'game1'.
        3. Multiple inheritance :- Multiple inheritance is the concept using which one sub class can inherit from more
    than one super class simultaneously. This can be understood as a sub class having multiple super class. For e.g, in
    the demo program the method 'game5' uses multiple inheritance as it inherits the methods of the classes 'game1' and
    'game2' both. Unlike multi level inheritance, in this concept we explicitly inherit from both classes.
    A super class is a class that has no predecessors i.e does not inherit any method or field from any other class. A
sub class is defined as a class that inherits from one or more class i.e has at least predecessor.

    Whenever an object is created via. instantiation then, the constructor method of that class is executed. In our
example, the class 'game1' is a predecessor of the other classes. Hence, whenever its sub classes do not contain a
constructor method then, the constructor method of the super class is executed. But, if the sub class has a constructor
method then, the sub class's constructor gets executed rather than the super class's constructor. In case if the
programmer wants the program to execute the constructors of both the super and sub class whenever the instance of sub
class is being created. For this the super function is used.
    If a class has multiple inheritance then, whenever the instance of the class is being created the class written to
the leftmost has its constructor executed. The associativity in this case is from left to right.
"""


class game1:

    def __init__(self):
        print("You're in A.")

    def feature1(self):
        print("Feature 1 working...")

    def feature2(self):
        print("Feature 2 working...")


class game2:

    def __init__(self):
        print("You're in B.")

    def feature3(self):
        print("feature 3 working...")

    def feature4(self):
        print("Feature 4 working...")


# example of single level inheritance
class game3(game1):

    def feature5(self):
        print("Feature 5 working...")

    def feature6(self):
        print("Feature 6 working...")


# example of multi level inheritance
class game4(game3):

    def __init__(self):
        print("You're in D.")

    def feature7(self):
        print("Feature 7 working...")

    def feature8(self):
        print("Feature 8 working...")


# example of multiple inheritance
class game5(game1, game2):

    def __init__(self):
        super(game5, self).__init__()
        print("You're in E.")

    def feature9(self):
        print("Feature 9 working...")

    def feature10(self):
        print("Feature 10 working...")


""" Run the program and you will find that in the first line the constructor of the 'game1' class is executed.
In second line, the constructor of 'game2' is executed. On line 3, the constructor of 'game3' should be executed but, as 
there is no constructor method defined in class 'game3'. Therefore, constructor of class 'game1' is executed as 'game3' 
is the sub class of 'game1' and 'game3' doesn't have a constructor. On line 4 the constructor of 'game4' is executed as 
the class 'game4' has its own constructor. If 'game4' didn't have a constructor then , the 'game3' constructor should be
executed as 'game4' inherits from 'game3' but even 'game3' doesn't have its own constructor and hence, the constructor 
of 'game1' should be executed. On the following line in the o/p window, the constructor of 'game5' is executed. Hence,
first of all the print statement inside 'game5' constructor is executed and next the the super() method is used to call 
the constructor of the super classes of 'game5'. This class has two parents and hence, the constructor of the left 
parent is executed by associativity.    """
g1 = game1()
g2 = game2()
g3 = game3()
g4 = game4()
g5 = game5()
''' as game1 and game2 classes don't have any predecessors, the objects of these classes can only access the methods 
inside of these classes'''
print("\t g1")
g1.feature1()
g1.feature2()
print("\t g2")
g2.feature3()
g2.feature4()
''' Observe that game3 has game1 as its predecessor and hence, can access all the methods from game1 but can't access 
any method from any other class'''
print("\t g3")
g3.feature1()
g3.feature2()
g3.feature5()
g3.feature6()
''' Here, the instance of game4 i.e g4 can access all the methods of class game3. Since, 'game3' also has a predecessor 
 i.e 'game1'. Hence, the methods in 'game1' are contained in the class 'game3' and therefore, 'game4' can also access 
 the methods in the class 'game1'.'''
print("\t g4")
g4.feature1()
g4.feature2()
g4.feature5()
g4.feature6()
g4.feature7()
g4.feature8()
''' In this case, 'game5' is the child/sub class of both 'game1' and 'game2'. Therefore, the class 'game5' can inherit
the methods of both the classes i.e class 'game1' and 'game2'.'''
print("\t g5")
g5.feature1()
g5.feature2()
g5.feature3()
g5.feature4()
g5.feature9()
g5.feature10()
