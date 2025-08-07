# Creating a TO-DO LIST

grocery_list = []

def menu():
    print(f'Welcome to my grocery list app!')
    print(f'1. Add to grocery list: ')
    print(f'2. Remove item')
    print(f'3. Display items / total cost')
    print(f'4. Quit and save to file')
    print(f'5. Quit')


def add_to_list():
    print("\nAdd items to grocery list:")

    item = input("What item would you like to add? ").strip().lower()

    try:
        quantity = int(input("Enter Quantity: "))
        price = float(input("How much does it cost? "))
    except ValueError:
        print("❌ Invalid input. Please enter numeric values for quantity and price.\n")
        return  # Exit early if input fails

    item_list = {
        'item': item,
        'price': price,
        'quantity': quantity
    }
    grocery_list.append(item_list)
    print("✅ Item added successfully!\n")

def display_info(finished_grocery_list):
    print("\nITEM LISTS:")
    # This formats the output ':<5'
    print(f"{'#':<5}{'Qty':<5} {'Item':<15} {'Price':<10} {'Cost':<10}")
    print("-" * 45)
    # iterates through and prints the contents of the list
    for i, item in enumerate(finished_grocery_list,1):
        item_total_cost = item['price'] * item['quantity']
        print(f"{i:<5}{item['quantity']:<5} {item['item']:<15} ${item['price']:<10} ${item_total_cost:<10}")
    # Calls the add_total() method to add the total cost of all the items in the list
    add_total(finished_grocery_list)

# This method adds the total cost of the items in the list
def add_total(total_cost):
    # total_cost_item is a placeholder for the total
    total_cost_of_items = 0
    # loop through the 
    for i in total_cost:
            total_cost_of_items += i['quantity'] * i['price']
    print(f'Total Cost: ${total_cost_of_items}')


def remove_item(finished_grocery_list):
    display_info(finished_grocery_list)
    item_to_be_removed = input("What item would you like to remove? ")
    for item in finished_grocery_list:
        if item['item'] == item_to_be_removed.lower().strip():
            grocery_list.remove(item)
        else:
            print("Item not in list.\n")

def save_to_file(filename, grocery_list_to_save):
    with open(filename, 'w') as file:
        file.write(f"{'#':<5}{'Qty':<5} {'Item':<15} {'Price':<10} {'Cost':<10}")
        file.write('\n' +"-" * 45 + '\n')
        for i, item in enumerate(grocery_list_to_save, 1):
            item_total_cost = item['price'] * item['quantity']
            file.write(f"{i:<5}{item['quantity']:<5} {item['item']:<15} ${item['price']:<10} ${item_total_cost:<10} \n")
        total_cost_of_items = 0
        for i in grocery_list_to_save:
            total_cost_of_items += i['quantity'] * i['price']
        file.write(f'Total Cost: ${str(total_cost_of_items)}')
    print("✅ File created/saved successfully!\n")

while True:
    menu()
    user_choice = int(input("Enter the number to the action you want to perform: "))
    if user_choice == 1:
        add_to_list()
    elif user_choice == 2:
        if not grocery_list:
            print("Error: Empty list, add items before you can remove an item (:\n")
        else:
            remove_item(grocery_list)
    elif user_choice == 3:
        display_info(grocery_list)
    elif user_choice == 4:
        if not grocery_list:
            print("Error: Empty list, add items before you can save to file (:\n")
        else:
            filename_user_gives = input("Save as(Must end in .txt):")
            save_to_file(filename_user_gives,grocery_list)

    else:
        print("Goodbye!")
        break