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
"""


class game1:

    def feature1(self):
        print("Feature 1 working...")

    def feature2(self):
        print("Feature 2 working...")


class game2:

    def feature3(self):
        print("feature 3 working...")

    def feature4(self):
        print("Feature 4 working...")


class game3(game1):

    def feature5(self):
        print("Feature 5 working...")

    def feature6(self):
        print("Feature 6 working...")


class game4(game3):

    def feature7(self):
        print("Feature 7 working...")

    def feature8(self):
        print("Feature 8 working...")


class game5(game1, game2):

    def feature9(self):
        print("Feature 9 working...")

    def feature10(self):
        print("Feature 10 working...")


g1 = game1()
g2 = game2()
g3 = game3()
g4 = game4()
g5 = game5()
''' as game1 and game2 classes don't have any predecessors, the objects of these classes can only access the methods 
inside of these classes'''
g1.feature1()
g1.feature2()
g2.feature3()
g2.feature4()
''' Observe that game3 has game1 as its predecessor and hence, can access all the methods from game1 but can't access 
any method from any other class'''
g3.feature1()
g3.feature2()
g3.feature5()
g3.feature6()
''' Here, the instance of game4 i.e g4 can access all the methods of class game3. Since, 'game3' also has a predecessor 
 i.e 'game1'. Hence, the methods in 'game1' are contained in the class 'game3' and therefore, 'game4' can also access 
 the methods in the class 'game1'.'''
g4.feature1()
g4.feature2()
g4.feature5()
g4.feature6()
g4.feature7()
g4.feature8()
''' In this case, 'game5' is the child/sub class of both 'game1' and 'game2'. Therefore, the class 'game5' can inherit
the methods of both the classes i.e class 'game1' and 'game2'.'''
g5.feature1()
g5.feature2()
g5.feature3()
g5.feature4()
g5.feature9()
g5.feature10()