#Quick intro into python

#asigning variables
num = 10
a = b = c = 100
string = "angel"
isItDark = True

#Global variables
#To modify a global variable you need to implicitly call global on the variable name
str = "Hello"

def fun():
    global str
    str += " World!"


fun()
print(str)

# using IN keyword
movies = {"The matrix","F1","Ford v Ferrari "}
user_input = input("Enter favorite movie:" )
print(user_input in movies)