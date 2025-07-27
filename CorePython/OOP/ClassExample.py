# Object Oriented Programming

# Creating a class called person
class Person:
    # defining the variables in my class called Person
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Displays The object values
    def display(self):
        return self.name, self.age

# Class Bank account example
class BankAcc:
    #constructor for BankAccInfo
    def __init__(self, name, age, gender, balance):
        self.name_ = name
        self.age_ = age
        self.gender_ = gender
        self.balance_ = balance

    # Created a Deposit function
    def deposit(self):
        amount = int(input("How much would you like to deposit?\n"))
        self.balance_ = self.balance_ + amount
        print(f"Deposited: ${amount}\nNew balance: ${self.balance_}\n")

    # Created a Withdraw function
    def withdraw(self):
        amount = int(input("How much would you like to withdraw?\n"))
        while amount > self.balance_:
            print(f"Insufficient funds. Available fund: {self.balance_}")
            amount = int(input("Now that you know your funds, how much would you like to withdraw? "))
        self.balance_ = self.balance_ - amount
        print(f"\nWithdrawed:{amount}")
        print(f"New balance after withdraw:{self.balance_}")

    # display information
    def displayaccinfo(self):
        print(f"Bank Account Information:\nName:{self.name_}\nAge:{self.age_}\nGender:{self.gender_}\nBalance:${self.balance_}")


