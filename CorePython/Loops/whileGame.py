number = 12
user_input = input("Do you want to play? Y/n ")

while user_input != 'n':
    user_guess = int(input("Guess the number:"))
    if user_guess == number:
        print("CONGRATULATIONS YOU WON A WHOLE LOTTA nothing!! ")
        break
    else:
        print("WRONG!")
    user_input = input("Do you want to guess again? Y/n ")