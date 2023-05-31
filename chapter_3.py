from utility.list_operations import *

list_of_fruits = ['apple', 'banana', 'orange', 'grapes', 'mango']
print('The list of fruits is: ', list_of_fruits)
print('Is apple in the list? ', search_item(list_of_fruits, 'apple'))

add_item(list_of_fruits, 'pear')
print('The list of fruits is: ', list_of_fruits)

remove_item(list_of_fruits, 'banana')
print('Is banana in the list? ', search_item(list_of_fruits, 'banana'))

