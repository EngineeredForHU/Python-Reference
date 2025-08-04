data_base = [
    {
        'name': 'Angel',
        'age': 24,
        'card_information': {
            'fname': 'Angel',
            'lname': 'Perez',
            'card_num': '1234122313',
            'cvv': '123',
            'expr_date': '08/28'
        },
        'shipping_address': {
            'address': '5727 w roma ave',
            'city': 'Phoenix',
            'state': 'Arizona',
            'zip_code': '85031'
        }
    },
    {
        'name': 'Samantha',
        'age': 30,
        'card_information': {
            'fname': 'Samantha',
            'lname': 'Lee',
            'card_num': '9876543210',
            'cvv': '456',
            'expr_date': '09/29'
        },
        'shipping_address': {
            'address': '1234 elm street',
            'city': 'Austin',
            'state': 'Texas',
            'zip_code': '73301'
        }
    }
]


print(data_base[0]['card_information']['cvv'])     # Angel's CVV
print(data_base[1]['shipping_address']['state'])   # Samantha's state


