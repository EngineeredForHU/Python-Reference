# Nested Loops Examples & Explanation
# For more information click the link below:
# https://www.geeksforgeeks.org/python/python-nested-loops/
# https://www.youtube.com/watch?v=tdjDQ-uVjR0

list_num1 = [1,2,3]
list_num2 = [4,5,6]

for i in list_num1:
    for j in list_num2:
        print(i,j)
    print()
print()

# This will print the multiplication table of 5
for i in range(5,6):
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print()
print()

# --------------------------
# Now I will showcase how to do it with a string

# Initialize list1 and list2
# with some strings
list1 = ['I am ', 'You are ']
list2 = ['healthy', 'fine', 'geek']

# Store length of list2 in list2_size
list2_size = len(list2)

# Running outer for loop to
# iterate through a list1.
for item in list1:

    # Printing outside inner loop
    print("start outer for loop ")
    # Initialize counter i with 0
    i = 0
    # Running inner While loop to
    # iterate through a list2.
    while(i < list2_size):

        # Printing inside inner loop
        print(item, list2[i])
        # Incrementing the value of i
        i = i+1
    # Printing outside inner loop
    print("end for loop ")
    print()