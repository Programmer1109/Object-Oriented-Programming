"""Object Oriented Programming(Tutorial 5)
    Inner class is a class inside another class. This type of a class is used whenever there is a need for a class to
hold a set of attributes that can itself form  a class. An inner class object is like an attribute for the outer class.

Now, if an instance of the Student class is to access the value of the Laptop class then, the syntax is
'student1.Laptop.
"""


class Student:

    def __init__(self, name, rollNo):
        self.name = name
        self.rollNo = rollNo
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollNo)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.brand = 'HP'
            self.cpu = '16GB'
            self.ram = '1TB'

        def show(self):
            print(self.brand, self.cpu, self.ram)


student1 = Student('Arwen', 4)
student2 = Student('Galadriel', 15)

lap1 = Student.Laptop()
lap2 = Student.Laptop()

student1.show()
student2.show()

lap1.show()
lap2.show()