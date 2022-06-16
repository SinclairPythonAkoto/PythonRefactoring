# Static and Class Methods #

'''
Class Method:   You do not need to create an object to access properties, you can
                call it on any instance of the class.
Static Method:  You don't need the self parameter (you don't need any parameters if you wanted).
                Static methods do not have access to class properties 
'''

class Person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')

newPerson = Person('John', 22)    # normal class object

print(newPerson.name)    # class object
print(Person.getPopulation())    # classmethod direct from class
print(Person.isAdult(60))        # staticmethod direct from class
print(Person.isAdult(2))



'''
Class Method:
    - You can call it on any instance of the class, you don't need to create an object
    - Takes the class then it can access the class properties
    - cls can be anythig needed to get access to class (like self), following convention
    - You need at least 1x parameter for the class method 
    - Within a class method you could call a static method

Static Method:
    - Good when you don't need self & you don't need a class object
    - You can use the static method by the name of the class and then the method name 
    - You don't need to use any parameters
'''
