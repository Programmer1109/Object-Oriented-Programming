''' Object Oriented Programming
     self :- It is object passed as an argument whenever a method in a class is used
     __init__ :- It is an acronym for instantiate. Whenever, the instance of a class i.e object is created this method
gets automatically called and executed. The concept of '__init__' method is exactly the same as constructor in object
oriented programming language.
'''


class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is:\n\tCPU :- ", self.cpu)
        print(f"\tRAM :- {self.ram}GB")


com1 = Computer('Intel i5', 16)  # creating an object of class Computer
com2 = Computer('Ryzen 3', 8)

''' This is a conventional way to access a method in the class of which com1 is an object. Here, we don't have to 
mention any argument as the it is the object itself that is accessing the member function from the class. '''
com1.config()
com2.config()

'''Another way to use the method in the class Computer. This is not the conventional way. Here,
we have to mention the argument 'com1' as we want to access but, its not clear for which object. This is because one 
class may have one or multiple instances or objects. '''
Computer.config(com1)
Computer.config(com2)
