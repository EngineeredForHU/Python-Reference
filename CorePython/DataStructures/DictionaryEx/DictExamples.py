person = [
    {"name": "Angel Perez", "age": 24,"gpa":3.9,"successful":True},
    {"name": "Gigi Lopez", "age": 22,"gpa":3.9,"successful":True},
    {"name": "Joe bruzzi", "age": 17,"gpa":3,"successful":True}
]

for i in person:

    print(f"{i["name"]}: Age: {i["age"]} {i["successful"]}")
    if i["age"] < 18:
        x = person.pop()
        print(f"Sorry {i["name"]}. but you're aren't old enough ):")