friends = [
    {"name":"Angel","age":24},
    {"name":"Gigi","age": 23}
]

for friend in friends:
    print(f"Friend: {friend["name"]} Age: {friend["age"]}")

for friend, age in friends.items():
    print(f"{friend} = {age}")