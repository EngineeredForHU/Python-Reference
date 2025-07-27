# animals.py

class Animal:
    '''Animal class with speak, move, and eat methods.'''
    def __init__(self, name="NoName"):
        print("ANIMAL: Constructor")
        self.name = name

    def speak(self):
        print("ANIMAL " + self.name + ": speaks")

    def move(self):
        print("ANIMAL " + self.name + ": I'm moving")

    def eat(self):
        print("ANIMAL " + self.name + ": I'm hungry!")


class Dog(Animal):
    '''Dog class extends Animal with fetch method.'''
    def __init__(self, name="NoName"):
        super().__init__(name)
        print("DOG: Constructor")

    def speak(self):
        print("DOG " + self.name + ": Woof! Woof!")

    def move(self):
        print("DOG " + self.name + ": I'm running!")

    def fetch(self):
        print("DOG " + self.name + ": Ball! Ball!")


class Cat(Animal):
    '''Cat class extends Animal.'''
    def __init__(self, name="NoName"):
        super().__init__(name)
        print("CAT: Constructor")

    def speak(self):
        print("CAT " + self.name + ": Meow!")

    def move(self):
        print("CAT " + self.name + ": Later")


class Parrot(Animal):

    def __init__(self, name="NoName"):
        super().__init__(name)
        print("Constructor")

    def speak(self):
        print("Parrot " + self.name + ":hey how are ya? hey how are ya?")

    def move(self):
        print("PARROT " + self.name + ": I'm flying around!")


if __name__ == "__main__":
    print("MAIN: Animal list example")
    animals = [
        Animal("George"),
        Dog("Spot"),
        Cat("Eek"),
        Parrot("Polly")
    ]
    for animal in animals:
        animal.speak()
        animal.move()
