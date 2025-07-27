# Running code will help you understand how the code works
# These are some examples of List Comprehension in python
# For more information follow the link below.
# https://www.geeksforgeeks.org/python/python-list-comprehension/

print()
numbers = [1,3,5]
print(f"ORIGINAL LIST{numbers}")
print("Example doubling a list of values by multiplying by 2:")
# looping through a list and doubling the value
doubled = [val * val for val in numbers]
print(doubled)
print()

#-----------------------------------------------------
print("--------------------------------\n")

# Now I will demonstrate how to loop through a list of strings
names = ["angel","gigi","Judy","Juan","Ari","mike"]
print(f"ORIGINAL LIST:{names}")
print()
print("Looping through a list and taking out the STRINGS that have the letter `a`:")
# This is looping through the list names and checking if any of the names are equal to "a" and assigning them to new_list
new_list = [name for name in names if "a" in name]
#Printing the new_list
print(new_list)
print()


# This basically prints everything that is not "Judy"
print("This loops through the list of strings and prints everything that is not Judy:")
new_list2 = [name2 for name2 in names if name2 != "Judy"]
print(new_list2)
print()

#---------------------------------------------------------------
print("--------------------------------\n")
# You also don't need a conditional statement
print("Not having a conditional will make the same list and assigning it to another variable you assigned:")
new_list3 = [name3 for name3 in names]
print(new_list3)

# --------------------------------------------------------------
print()
print("------------------------------")
print()

nums2 = [1,2,3,4,5,6,7,8,9,10]
evenNums = [num for num in nums2 if num % 2 == 0]
print(evenNums)

strings = ["ANGEL","bob","Abe","Shotzzy", "Jesus"]
name_check = [name for name in strings if name.lower().startswith("a")]
print(name_check)

# Will be using the nums list above
# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
new_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(new_list)