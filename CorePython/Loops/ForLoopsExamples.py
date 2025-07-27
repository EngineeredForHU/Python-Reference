# For-loops are used for sequential traversal.
# Examples include: traversing a list or string or an array, etc.

# Basic loop
#print("Basic Loop")
#n = 4
#for i in range(0, n):
#    print(i)
#print()

# EXAMPLE with List, Tuple, String, and Dictionary iteration using for loops in Python
print("\nEXAMPLES with List, Tuple, String, and Dictionary iteration using for loops in Python **BELOW**")

# List Example
print("\nList Example:")
li = ["Angel", "Gigi", "For"]
for i in li:
    print(i)

# Tuple Example
print("\nTuple Example:")
tup = ("Immutable","after","assigning")
for i in tup:
    print(i)

# String Example
print("\nString Example:")
string = "BEAST"
for i in string:
    print(i)

# Dictionary Example
print("\nDictionary Example:")
# Creating a dictionary
di = dict({'x':123, 'y':69})
#looping in di
for i in di:
    print("%s %d" % (i, di[i]))