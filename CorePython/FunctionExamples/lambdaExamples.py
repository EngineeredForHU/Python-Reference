# Several Examples of lambda functions


# Basic Example of lambda
print("Basic Lambda Function:")
str1 = 'Angel Perez'
# This lambda function takes in a string as it's argument and converts it to uppercase using the upper()
lam2 = lambda func: func.upper()
print(lam2(str1))
print("-----------------------")

print("Using integers with Lambda:")
nums = 12
print(f"Original value: {nums}")
# This lambda function takes in a integer as it argument and multiplies it by 2
lam3 = lambda li: li * 2
print(f"After using Lambda:\nnums * 2 = {lam3(nums)}")

# Lets now reuse that lambda function FROM ABOVE
print()
print("Using the previous lambda function on a new variable:")
new_number = 5
print(f"Original value: {new_number}")
print(lam3(new_number))

print("-----------------------")

# Now These examples are including condition checking
print("Examples of using condition checking:")
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
# now let's test our logic above
print(n(-1))
print(n(2))
print(n(0))
print("-----------------------")

# Now we look at how to use list comprehensions with lambda
print("list comprehension with lambda:")

li = [lambda arg=x: arg * 10 for x in range(1,5)]
for i in li:
    print(i())
