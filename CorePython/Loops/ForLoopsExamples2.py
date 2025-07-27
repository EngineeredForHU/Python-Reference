# More examples of For Loops in Python
# For more information copy and paste link Below:
# https://www.geeksforgeeks.org/python/python-for-loops/#python-for-loop-with-string

# Looping through a string
print("String Examples:")
string = "Optic"
for i in string:
    print(f"{i}", end="-")
print()

#--------------------------

# Creating a List of Movies & using a for loop
print("-----------------")
movies = ["Matrix","F1","Titanic"]
print(f"Creating a List of Movies:{movies}")
# Now I will iterate the List and print them
for i in movies:
    # Here end=" " will add a space between iterations after it will print a new line
    print(i, end=" ")
print()

# ----------------------------

print("-----------------")
# the Enumerate function loops over an iterable(list,dict,tuple..) while keeping track of the index.
print("Enumerate Examples:")
# Created a list [] called li
li = ["eat","code", "sleep","repeat"]
print(f"ORIGINAL LIST:{li}")
#Now I will loop through this list with ENUMERATE
#`i` is the index, and `j` is the value at that index
for i, j in enumerate(li):
    print(f"[{i}]{j}")

