# This will be an example of class attributes
# Classmethod
class Person:
    # This won't change with different instances of the object Person
    number_of_people = 0

    def __init__(self, name):
        # because this has self. it will change with different instances of Person
        self.name = name
        # This keeps track of how many instances have been created.
        Person.add1()

    @classmethod
    def add1(cls):
        cls.number_of_people += 1


p1 = Person("tim")
p2 = Person("Bob")
print(Person.number_of_people)

# Example of staticMethod
class MathOp:
    @staticmethod
    def add_(x):
        return x + x

print(MathOp.add_(5))