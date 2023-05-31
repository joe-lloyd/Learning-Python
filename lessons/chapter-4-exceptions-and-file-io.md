## Chapter 4: Exception Handling & File I/O

### 4.1 Exception Handling
While running a python program, errors can occur, these are called exceptions. They can be handled using try-except blocks.

**Try-Except Blocks**: Python uses try and except keywords to manage exceptions. The code which can cause an exception to occur is put in a try block and the handling of the exception is then implemented in an except block of code.

```python
try:
    # code that could raise an exception
    x = 1 / 0
except ZeroDivisionError:
    # code that runs if the exception occurs
    print("You can't divide by zero!")
```

Python also allows the use of `else` and `finally` clauses in exception handling.

### 4.2 File I/O
Python allows you to read from and write to files on your system. This is done using the built-in `open()` function, which returns a file object.

- **Reading from a File**: Use the `'r'` mode with `open()` to read from a file.

```python
file = open('myfile.txt', 'r')
content = file.read()  # reads the entire file
file.close()
```

- **Writing to a File**: Use the `'w'` mode with `open()` to write to a file. This will overwrite any existing content in the file.

```python
file = open('myfile.txt', 'w')
file.write("Hello, World!")
file.close()
```

- **Appending to a File**: Use the `'a'` mode with `open()` to append to a file. This will add to the end of the file's existing content.

```python
file = open('myfile.txt', 'a')
file.write("\nGoodbye, World!")
file.close()
```

It's important to always close files after you're done with them, as they consume system resources. Python provides the `with` keyword, which automatically manages resources for you.

```python
with open('myfile.txt', 'r') as file:
    content = file.read()
```

### 4.3 Mini-Project: Write a program to manage a text file.
The goal of this mini-project is to create a program that allows the user to manage a text file. This should include reading from the file, writing to the file, and handling any potential exceptions that occur.

Here's a breakdown of the mini-project:

1. Prompt the user to enter the name of a text file.
2. Prompt the user to choose an operation: read from the file, write to the file, or append to the file.
3. Use a try-except block to perform the operation and handle any exceptions that occur (e.g., if the file does not exist).
4. Repeat steps 2-3 until the user chooses to exit the program.

By the end of this chapter, you will understand how to handle exceptions in Python, which will help you build more robust programs. You'll also know how to work with files, which is a crucial skill for many types of Python programs.