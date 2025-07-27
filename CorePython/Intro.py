strings = [
    {"name":"angel","age":23},
    {"name":"angel","age":25},
    {"name":"angel","age":27},
]
print(strings[0]["name"])

for i in strings:
    print(f"{i["age"]}", end =" ")

print()
nums = [1,2,3,4,5]
new_nums = [num * 2 for num in nums]
print(new_nums)

num_dict = {}