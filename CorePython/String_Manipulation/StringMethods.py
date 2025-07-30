# This is an introduction to string manipulation in python
# NOTE IMPORTANT: Every string method in python does not change the original string instead returns a new string with the changed attributes
# These are basic examples of manipulating strings in python for more practical examples will be in StringMethods2.py

# Here are examples of Case Changing
# Using .upper() method
name = "Angel Perez"
print("Using .upper() method:")
print(f"Original String: {name}")
print(f"Changing String to uppercase using .upper(): {name.upper()}")

print("-----------")

# Using .lower() method
angry_expression = "HEY!!"
print("Using .lower() method:")
print(f"Original String: {angry_expression}")
print(f"Changing String to uppercase using .upper(): {angry_expression.lower()}")

print("-----------")

# Using .title() method
movie = "ford vs ferrari"
print("Using .title() method:")
print(f"Original String: {movie} (movies should be capitalized)")
print(f"Changing String to uppercase using .title(): {movie.title()}")

print("-----------")

# using swapcase() method
loud = "AAAAHHHHH"
print(f"Using .swapcase() method:")
print(f"Original String: {loud} (Changing the cases SWAP)")
print(f"Changning String case using swapcase(): {loud.swapcase()}")

print("-----------")

# Using capitalize() method
names = "angel perez"
print("Using .capitalize() method:")
print(f"Original String: {name}")
print(f"Changing String to uppercase using .capitalize(): {names.capitalize()}")
