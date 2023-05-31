# Set of functions to perform list operations used in chapter 3

# Function to add an item to the list
def add_item(item_list, item):
    item_list.append(item)
    return item_list


# Function to remove an item from the list
def remove_item(item_list, item):
    item_list.remove(item)
    return item_list


# Function to search for an item in the list
def search_item(item_list, item):
    if item in item_list:
        return True
    else:
        return False
