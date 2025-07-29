class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    # This turns the object into a string and describes the object
    def __str__(self):
        return f"{self.name}, {self.age} years old."

    # Has to do with the debugger
    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"

bob = Person("bob", 55)
angel = Person("angel",24)
print(angel)
print(bob)