''' Object Oriented Programming (Tutorial 2)
    self :- This is like a pointer to the object declared using the class name. Hence, self refers to the object that is
accessing the class method.
'''


class Employee:
    def __init__(self, name= "Anto", age = 21, race='human'):
        self.name = name
        self.age = age
        self.race = race

    def display(self):
        print("Employee Details:-\n\tName:- ", self.name)
        print("\tAge:- ", self.age)
        print("\tRace:- ", self.race)

    def update(self):
        self.age = self.age + 2

    def compare(self, other):
        if self.age > other.age:
            print(f"{self.name} is older than {other.name}")
        elif self.age < other.age:
            print(f"{self.name} is younger than {other.name}")
        else:
            print(f"{self.name} is the same age as {other.name}")


# Declaring objects using the class Employee
emp1 = Employee('Frodo', 35, 'Hobbit')
emp2 = Employee('Legolas', 52, 'Elf')
emp3 = Employee('Aragorn', 80, 'Numenor')

emp1.display()
Employee.display(emp2)
emp3.update()
emp3.display()

emp1.compare(emp2)
emp2.compare(emp1)
emp2.compare(emp3)
emp3.compare(emp2)
emp3.compare(emp1)
emp1.compare(emp3)
