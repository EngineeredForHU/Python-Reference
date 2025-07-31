students = [
    {
        "name": "Adriana",
        "age": 22,
        "major": "Nursing",
        "address": {"city": "Phoenix", "state": "AZ"}
    },
    {
        "name": "Carlos",
        "age": 23,
        "major": "Biology",
        "address": {"city": "Tucson", "state": "AZ"}
    },
]

print(students[0]["address"]["city"])


api_response = {
    "user": {
        "username": "adriana22",
        "email": "adriana@example.com",
        "profile": {
            "full_name": "Adriana Lopez",
            "location": {
                "city": "Phoenix",
                "state": "AZ"
            },
            "interests": ["nursing", "fitness", "F1"]
        }
    }
}

print(f'{api_response["user"]["profile"]["full_name"]} is from {api_response["user"]["profile"]["location"]["city"]} {api_response["user"]["profile"]["location"]["state"]}')
print(f'{api_response["user"]["profile"]["full_name"]} enjoys {api_response["user"]["profile"]["interests"][0]} and {api_response["user"]["profile"]["interests"][1]}')