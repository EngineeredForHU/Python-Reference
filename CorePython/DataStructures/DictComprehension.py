# Few examples of using comprehension with dict
# For more information:
# https://www.geeksforgeeks.org/python/python-dictionary-comprehension/

# First basic example:
#This is a simple example
myDict = {num: num**2 for num in [1,2,3,4]}
print(myDict)

# Second example:
names = ['bruce','Clark','Peter','Logan']
heros = ['Batman',"Superman","Spiderman", "Wolverine"]

myDict2 = {name:hero for name, hero in zip(names,heros)}
print(myDict2)
print(myDict2["bruce"])
