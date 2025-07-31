# These examples include for loops, string methods, String Slicing,
# For more information follow the link below:
#

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

# Finding all the names that start with a vowel EXPLAINED BELOW:
# Created an empty list to append the names that have vowels
print("Finding the names that start with a vowel:")
list_1 = []
# Loops through the list and assigns it to name
for name in names:
    # checking if the starting letter in the word starts with a vowel
    if name[0].lower() in ['a','e','i','o','u']:
        # Appending the words that start with a vowel to the new list(li)
        list_1.append(name)
print(list_1)

print("------------")


# Reversing each name and storing it in a new list
print("Reversing the name in the list:")
list_2 = []
for name in names:
    reverse_word = name[::-1]
    list_2.append(reverse_word)
print(list_2)

print("------------")

# Find all names that end with the letter 'n'
print("Finding the names that end with a 'n': ")
list_3 = []
for name in names:
    if name[-1].lower() == 'n':
        list_3.append(name)
print(list_3)

print("------------")

# Finding the longest name in the list
print("Finding the longest name in the list:")
longest = ""
for name in names:
    if len(name) > len(longest):
        longest = name

print(longest)

