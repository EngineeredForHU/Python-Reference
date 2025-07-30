# This file will have more practical examples of manipulating strings in lists, dicts, sets etc
# For more information follow the link below:
#
# This is a fake list for practice
names = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana",
    "Evelyn",
    "Franklin",
    "Grace",
    "HUGO",
    "Isabella",
    "Jack",
    "Katherine",
    "Liam",
    "Mona",
    "Nathan",
    "Olivia",
    "Preston",
    "Quincy",
    "Rachel",
    "Samuel",
    "Tina"
]

# Now I will demonstrate how to find a certain name; Using for loop and string manipulation
print("Finding a name in a list:")
for name in names:
    lower_name = name.lower()
    if lower_name == 'hugo':
        print(f"<{lower_name}> was found in the list")


print("--------------")

# Now I will change all names to uppercase
print(f"Changing names to uppercase:")
for name in names:
    upper_name = name.upper()
    print(f"{upper_name}", end=" ")

print("\n--------------")

# Now I will count the names that are longer than 5 characters
print(f"Counting the names that are longer than 5 characters long:")
print("Used list comprehension to count the names longer than 5:")
li = [name for name in names if len(name) > 5]
print(f"{li}")

print()

print("Then I ran the list(li) in a loop to print w/o the list for a cleaner look:")
print("NAMES > 5:")
for i in li:
    print(f"{i}", end=", ")











