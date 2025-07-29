def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total
print(multiply(1,2,3))

print("--------------------")

# Just a basic function that adds two variables
def add(x,y):
    return x + y

# this unpacks the arguments 3 and 5 so it can be passed to the function as x and y
nums = [3,5]
print(add(*nums))

# Can also be used in a dict
dict_nums2 = {"x":15,"y":10}

# Notice there are two asterisks
print(add(**dict_nums2))