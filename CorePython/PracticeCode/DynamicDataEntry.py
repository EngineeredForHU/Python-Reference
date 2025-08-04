# This file will show basic Dynamic Data Entry from prompting the user
data_base = []

def add_user():
    print("Enter User Information")
    name = input("Enter name: ")
    email = input("Enter Email: ")

    print("Enter Credit Card Information: ")
    full_name = input("Enter Full Name: ")
    credit_card_number = input("Enter credit card number: ")
    cvv_number = int(input("Enter CVV: "))
    expire_date = int(input("Enter Expiration Date: "))

    print("Shipping Information")
    address = input("Enter shipping address: ")
    city = input("Enter City:")
    state = input("Enter State:")
    zip_code = int(input("Enter zip code:"))

    new_user = {
        'name':name,
        'email': email,
        'card_information': {
            'full_name':full_name,
            'credit_card_number': credit_card_number,
            'cvv_number': cvv_number,
            'expire_date': expire_date
        },
        'shipping_address':{
            'address': address,
            'city':city,
            'state':state,
            'zip_code':zip_code
        }
    }

    data_base.append(new_user)
    print("\nUser added successfully!\n")

while True:
    add_user()
    another_user = input("Add another user? (Y/n): ").strip().lower()
    if another_user != 'y':
        break

for i, user in enumerate(data_base,1):
    print(f'\nUser {i}:')
    print(user)