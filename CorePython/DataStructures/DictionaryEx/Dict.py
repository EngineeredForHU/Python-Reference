#Example of a dictionary in python

#implicitly
friend_ages = {"Rolf":24,"name":"Angel","Anne":40}
#explicitly
friend_hair_color = dict(brown = "Rolf",blue = "Adam")
print(friend_hair_color["brown"])

# Accessing one
print(friend_ages["name"])

############################################################

# A more practical approach
# using a dictionary within a list
friends = [
    {"name":"Rolf","age":24},
    {"name": "Adam","age":30},
    {"name": "Anne","age":27}
]
print(friends)

# indexing
print(friends[1]["name"])
print(friends[1]["age"])

print()
############################################################

# iterating through a dict

student_attendance = {"rolf":96,"Bob":80,"Anne":100}

for student in student_attendance:
    print(f"{student} attendance: {student_attendance[student]}%")

# better way is
print()
for student, attendance in student_attendance.items():
    print(f"{student}:{attendance}")

