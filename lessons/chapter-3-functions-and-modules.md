## Chapter 3: Functions and Modules

### 3.1 Defining and Calling Functions
Functions in Python are blocks of reusable code that perform a specific task. You define a function using the `def` keyword, followed by a function name, parentheses `()`, and a colon `:`. The code block within every function is indented.

```python
def greet():
    print("Hello, World!")
```

To call a function, you simply write the function's name followed by parentheses.

```python
greet()  # Outputs: Hello, World!
```

### 3.2 Parameters and Return Values
Functions can take inputs, known as parameters, and return outputs, known as return values.

**Parameters** are specified after the function name, inside the parentheses. You can add as many parameters as you want, just separate them with a comma.

```python
def greet(name):
    print(f"Hello, {name}!")
```

A **return** statement is used to exit a function and go back to the place from where it was called. Functions in Python can optionally return values. This allows the function to produce outputs that can be stored or used for further computation.

```python
def add(a, b):
    return a + b
```

### 3.3 Built-in Functions and Modules
Python comes with a set of built-in functions and modules that are available for use without any additional import statements. Some commonly used built-in functions include `print()`, `len()`, `type()`, `str()`, `int()`, `input()`, and so on.

Python also has many built-in modules that provide useful functionalities. For example, the `math` module provides mathematical functions, the `datetime` module provides functions for manipulating dates and times, and so on.

To use a module, you must first import it using the `import` keyword.

```python
import math
print(math.sqrt(16))  # Outputs: 4.0
```

### 3.4 Creating and Importing Your Own Modules
A module is simply a file containing Python definitions and statements. You can create your own modules, and then import them into other scripts as needed. This is great for organizing and reusing code.

Here's an example of how you might create and use a custom module.

1. Create a new Python file named `mymodule.py`.
2. In `mymodule.py`, define a function.

```python
# mymodule.py

def greet(name):
    print(f"Hello, {name}!")
```

3. In another Python file, import and use the `mymodule`.

```python
import mymodule

mymodule.greet("Alice")
```

### 3.5 Mini-Project: Write a module that performs operations on a list
The goal of this mini-project is to create a Python module that provides a set of functions for performing operations on a list, such as add (append), remove, and search. This will allow you to practice defining and using functions and modules.

Here's a breakdown of the mini-project:

1. Create a new Python file named `list_operations.py`.
2. In `list_operations.py`, define several functions: `add_item()`, `remove_item()`, and `search_item()`.
3. Each function should accept a list and one or more additional parameters, perform an operation on the list, and then return the modified list (if applicable).
4. In a separate Python file, import `list_operations` and use its functions to manipulate a list.

By the end of this chapter, you will be comfortable defining your own functions and

 modules, and using built-in Python functions and modules. You'll also be able to organize your code more effectively and make it more reusable.
