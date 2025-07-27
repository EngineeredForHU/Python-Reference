"""
# using IN keyword
movies = {"The matrix","F1","Ford v Ferrari "}
user_input = input("Enter favorite movie:" )
print(user_input in movies)

# using if with in Keyword
genre = {"piano","hip-hop","r&b"}
user_genre = input("Favorite Genre of music: ")

if user_genre.lower() in genre:
    print(f"We both like {user_genre} music")
else:
    print("I don't like that genre")
"""


number = 7
user = input("Enter 'y' to start game: ").lower()

if user == "y":
    user_number = int(input("guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by one!")
    else:
        print("Sorry, wrong")
