#example of using/creating a list

# the list A can contain any data types
# square brackets denote that it's a list
A = [10, 20, "LFG",40, True]
print(A)

# Accessing elements using indexing
print("Indexing Individual elements")
print(A[0])
print(A[1])
print(A[2])
print(A[3])
print(A[4])

print()

# Checks the type
print("Data Types:")
print(type(A[0]))
print(type(A[1]))
print(type(A[2]))
print(type(A[3]))
print(type(A[4]))

# List of integers
a = [1, 2, 3, 4, 5]

# List of strings
b = ['apple', 'banana', 'cherry']

# Mixed data types
c = [1, 'hello', 3.14, True]

print(a)
print(b)
print(c)

print()

# going from a tuple to list, using a list constructor
A2 = list((1,2,3,'hello', 4.5))
print(A2)


# Initialize an empty list
A3 = []

# Adding 10 to end of list
A3.append(10)
print("After append(10):", a)

# Inserting 5 at index 0
A3.insert(0, 5)
print("After insert(0, 5):", a)

# Adding multiple elements [15, 20, 25] at the end
A3.extend([15, 20, 25])
print("After extend([15, 20, 25]):", a)

a = [10, 20, 30, 40, 50]

# Removes the first occurrence of 30
a.remove(30)
print("After remove(30):", a)

# Removes the element at index 1 (20)
popped_val = a.pop(1)
print("Popped element:", popped_val)
print("After pop(1):", a)

# Deletes the first element (10)
del a[0]
print("After del a[0]:", a)