# Creating a TO-DO LIST

grocery_list = []

def add_to_list ():
    print("Add items to grocery list:")
    item = input("What item would you like to add? ")
    price = float(input("How much does it cost? "))

    item_list = {
        'item': item,
        'price': price
    }
    grocery_list.append(item_list)
    print("Added item successfully!")

def display_info(finished_grocery_list):
    print("Item List:")
    for i, item in enumerate(finished_grocery_list,0):
        print(f"{item['item']}: ${item['price']} ")
    add_total(finished_grocery_list)

def add_total(total_cost):
    total_cost_of_items = 0
    for i in total_cost:
        total_cost_of_items += i['price']
    print(f'Total sum: ${total_cost_of_items}')



while True:
    add_to_list()
    another_user = input("Do you want to enter another item? Y/n ").strip().lower()
    if another_user != 'y':
        print()
        display_info(grocery_list)
        break
