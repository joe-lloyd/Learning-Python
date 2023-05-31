# Function to create an empty shopping list
def create_list():
    shopping_list = []
    return shopping_list


# Function to add an item to the shopping list
def add_item(shopping_list, item):
    shopping_list.append(item)
    return shopping_list


# Function to remove an item from the shopping list
def remove_item(shopping_list, item):
    shopping_list.remove(item)
    return shopping_list


# Function to print the shopping list
def print_list(shopping_list):
    for item in shopping_list:
        print(item)


# Function to print the menu
def print_menu():
    print('0 - Main Menu')
    print('1 - Show current list')
    print('2 - Add an item to your shopping list')
    print('3 - Remove an item from your shopping list')
    print('4 - Sort alphabetically')
    print('5 - Exit')


# Function to sort the list alphabetically
def sort_list(shopping_list):
    shopping_list.sort()
    return shopping_list


# Function to get the user's choice
def get_choice():
    valid_choices = ['0', '1', '2', '3', '4', '5']
    choice = input('Please enter a valid choice: ')
    while choice not in valid_choices:
        choice = input('Please enter a valid choice: ')
    return choice


# Function to get the item to add to the shopping list
def get_item():
    item = input('Please enter the item: ')
    return item


# Function to get the item to remove from the shopping list
def get_item_to_remove():
    item = input('Please enter the item to remove: ')
    return item


# Function to run the program
def main():
    shopping_list = create_list()
    print_menu()
    choice = get_choice()
    while choice != '5':
        if choice == '0':
            print_menu()
        elif choice == '1':
            print_list(shopping_list)
        elif choice == '2':
            item = get_item()
            shopping_list = add_item(shopping_list, item)
        elif choice == '3':
            item = get_item_to_remove()
            shopping_list = remove_item(shopping_list, item)
        elif choice == '4':
            shopping_list = sort_list(shopping_list)
            print_list(shopping_list)
        choice = get_choice()
    print('Thank you for using the shopping list program.')


# Call the main function
main()
