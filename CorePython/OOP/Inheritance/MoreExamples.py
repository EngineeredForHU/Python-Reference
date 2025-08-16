# More examples of inheritance
class Animal:
    def __init__(self, animal_name, weight, breed, gender):
        self.animal_name = animal_name
        self.weight = weight
        self.breed = breed
        self.gender = gender

    def __str__(self):
        return (f"{self.animal_name}:\n"
                f"Weight: {self.weight} lb\n"
                f"Animal: {self.animal_name}\n"
                f"breed: {self.breed}\n"
                f"Gender: {self.gender}")

    def eat(self):
        return f'{self.animal_name} is eating'
    def sleep(self):
        return f'{self.animal_name} is sleeping'

class Dog(Animal):
    def __init__(self, animal_name, weight, breed, gender):
        super().__init__(animal_name, weight, breed,gender)

    def bark(self) -> str:
        return f"{self.animal_name}: **Barks**"

class Chicken(Animal):
    def __init__(self, animal_name, weight, color, breed, gender):
        super().__init__(animal_name, weight,breed,gender)
        self.color = color
    def color_of_chicken(self):
        return f"The color of this chicken is {self.color}"


d1 = Dog("Diamond",40,"corgi","Male")
print(d1)

c1 = Chicken("james",8,"Red/Black","Ga Noi","Male")
print(f"\n{c1}")