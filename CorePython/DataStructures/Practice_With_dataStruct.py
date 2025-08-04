# Creating a TO-DO LIST

grocery_list = []

def add_to_list ():
    print("Add items to grocery list:")
    item = input("What item would you like to add? ")
    quantity = int(input("Enter Quantity: "))
    price = float(input("How much does it cost? "))

    item_list = {
        'item': item,
        'price': price,
        'quantity':quantity
    }
    grocery_list.append(item_list)
    print("Added item successfully!")

def display_info(finished_grocery_list):
    print(f"{'Qty':<5} {'Item':<15} {'Price':<10}")
    print("-" * 45)
    for i, item in enumerate(finished_grocery_list,0):
        print(f"{item['quantity']:<5} {item['item']:<15} ${item['price']:<10}")
    add_total(finished_grocery_list)

def add_total(total_cost):
    total_cost_of_items = 0
    for i in total_cost:
        if i['quantity'] > 1:
            total_cost_of_items += i['quantity'] * i['price']
        else:
            total_cost_of_items += i['price']
    print(f'Total cost: ${total_cost_of_items}')


while True:
    add_to_list()
    another_user = input("Do you want to enter another item? Y/n ").strip().lower()
    if another_user != 'y':
        print()
        display_info(grocery_list)
        break
