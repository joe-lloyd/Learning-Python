## Chapter 2: Data Structures

### 2.1 Lists and Tuples
Lists and tuples are ordered collections of items. Lists are mutable (changeable), whereas tuples are immutable (unchangeable).

**Lists**: A list is defined by enclosing a comma-separated sequence of objects in square brackets (`[]`), like so: `my_list = [1, 2, 3, "apple", "banana"]`.

**Tuples**: A tuple is defined by enclosing a comma-separated sequence of objects in parentheses (`()`), like so: `my_tuple = (1, 2, 3, "apple", "banana")`.

### 2.2 Sets and Dictionaries
Sets and dictionaries are unordered collections of items. Sets store unique items, while dictionaries associate keys with values.

**Sets**: A set is an unordered collection of unique items. Set is defined by values separated by a comma inside braces `{}`, like so: `my_set = {1, 2, 3, "apple", "banana"}`.

**Dictionaries**: A dictionary is an unordered collection of key-value pairs. Dictionaries are defined by comma-separated key:value pairs within braces `{}`, like so: `my_dict = {"key1": "value1", "key2": "value2"}`.

### 2.3 Data Structure Methods
Python provides several methods that allow you to manipulate these data structures:

- Lists: `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `clear()`, `index()`, `count()`, `sort()`, `reverse()`, and others.
- Tuples: `count()`, `index()`.
- Sets: `add()`, `update()`, `remove()`, `discard()`, `clear()`, `union()`, `intersection()`, `difference()`, and others.
- Dictionaries: `get()`, `keys()`, `values()`, `items()`, `update()`, `clear()`, and others.

### 2.4 Iterations (Loops) and Comprehensions
Iterations allow you to execute a block of code several times. Python has two primitive loop commands:

- `for` loops: A `for` loop is used for iterating over a sequence (like a list, tuple, dictionary, set, or string).
- `while` loops: With the `while` loop we can execute a set of statements as long as a condition is true.

Python also provides a feature called 'comprehensions' (list comprehension, dictionary comprehension, set comprehension) that allow you to create lists, dictionaries, and sets from other iterables in a concise and efficient way.

### 2.5 Mini-Project: Write a program to manipulate a shopping list
The goal of this mini-project is to create a program that allows the user to manage a shopping list. This should reinforce your understanding of data structures and iterations.

Here's a breakdown of the mini-project:

1. Create an empty shopping list.
2. Prompt the user to add an item to the shopping list.
3. Prompt the user to remove an item from the shopping list.
4. Prompt the user to view all items in the shopping list.
5. Prompt the user to sort the shopping list.
6. Repeat steps 2-5 until the user chooses to exit the program.

By the end of this chapter, you will have a solid understanding of Python's basic data structures, how to manipulate them, and how to create loops and comprehensions. These skills are fundamental to solving many different types of problems in Python.