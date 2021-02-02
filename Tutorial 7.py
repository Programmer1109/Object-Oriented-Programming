''' Object Oriented Programming (Tutorial 7)
    Whenever an object is created via. instantiation then, the constructor method of that class is executed. In our
example, the class 'game1' is a predecessor of the other classes. Hence, whenever its sub classes do not contain a
constructor method then, the constructor method of the super class is executed. But, if the sub class has a constructor
method then, the sub class's constructor gets executed rather than the super class's constructor. In case if the
programmer wants the program to execute the constructors of both the super and sub class whenever the instance of sub
class is being created. For this the super function is used.
    If a class has multiple inheritance then, whenever the instance of the class is being created the class written to
the leftmost has its constructor executed. The associativity in this case is from left to right.
'''


class game1:

    def __init__(self):
        print("You're in A.")

    def feature1(self):
        print("Feature 1 working...")

    def feature2(self):
        print("Feature 2 working...")


class game2(game1):

    def __init__(self):
        print("You're in B.")
        super().__init__()

    def feature3(self):
        print("feature 3 working...")

    def feature4(self):
        print("Feature 4 working...")


class game3(game1):

    def feature5(self):
        print("Feature 5 working...")

    def feature6(self):
        print("Feature 6 working...")


class game4():

    def __init__(self):
        print("You're in D.")

    def feature7(self):
        print("Feature 5 working...")

    def feature8(self):
        print("Feature 6 working...")


class game5(game4, game1):

    def __init__(self):
        super(game5, self).__init__()
        print("You're in E.")

    def feature9(self):
        print("Feature 9 working...")

    def feature10(self):
        print("Feature 10 working...")


g1 = game1()
g2 = game2()
g3 = game3()
g5 = game5()