""" Object Oriented Programming (Tutorial 3)
    'namespace' is the area where you create and store objects/variable. There are two different namespaces 'class
    namespace' and 'instance/object namespace' respectively.
        1. instance variable :- These are the variables which are contained in the '__init__' method and are not
necessarily same for all the objects created using the same class name. The values of these variables can be changed
using the individual object and the changes made to this object will not affect the value contained by some other object
of the same class.
       2. class/static variable :- These are the variables which are contained inside the scope of the class but,
outside the any of the member functions. Also, it is important to note that any change made to these variables directly
affects the other objects created using the same class name if that assignment is done using the class name. Hence, the
value stored in this variable is common to all the objects which are the instances of the same class.
"""


class Car:
    wheels = 4

    def __init__(self):
        self.mil = 10
        self.company = 'Tesla'
        self.maxSpeed = 135


porsche911 = Car()
beat = Car()
golf = Car()

print("\nOriginal values :-")
print(f"\t Company :- {porsche911.company}\n\t Mileage :- {porsche911.mil}\n\t Max Speed :- {porsche911.maxSpeed}\n")
print(f"\t Company :- {beat.company}\n\t Mileage :- {beat.mil}\n\t Max Speed :- {beat.maxSpeed}\n")
print(f"\t Company :- {golf.company}\n\t Mileage :- {golf.mil}\n\t Max Speed :- {golf.maxSpeed}\n")

porsche911.mil = 13
porsche911.company = 'Porsche'
porsche911.maxSpeed = 150

beat.mil = 23
beat.company = 'Chevrolet'
beat.maxSpeed = 95

golf.mil = 17
golf.company = 'Volkswagen'
golf.maxSpeed = 110

print("\nUpdated Values:-")
print(f"\t Company :- {porsche911.company}\n\t Mileage :- {porsche911.mil}\n\t Max Speed :- {porsche911.maxSpeed}\n")
print(f"\t Company :- {beat.company}\n\t Mileage :- {beat.mil}\n\t Max Speed :- {beat.maxSpeed}\n")
print(f"\t Company :- {golf.company}\n\t Mileage :- {golf.mil}\n\t Max Speed :- {golf.maxSpeed}\n")

print("Before change Wheels :-")
print("\t porsche:- ", porsche911.wheels)
print("\t chevrolet :- ", beat.wheels)
print("\t volkswagen :- ", golf.wheels)
print("\t car :- ", Car.wheels)

Car.wheels = 5
print("After change Wheels :-")
print("\t porsche:- ", porsche911.wheels)
print("\t chevrolet :- ", beat.wheels)
print("\t volkswagen :- ", golf.wheels)
print("\t car :- ", Car.wheels)
