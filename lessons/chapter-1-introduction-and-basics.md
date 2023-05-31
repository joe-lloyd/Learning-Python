## Chapter 1: Introduction to Python & Basics

### 1.1 Installing Python and Setting Up the Development Environment
Before you start programming, you'll need to install Python on your computer and set up a development environment.

#### Installing Python:
- Visit the official Python website at www.python.org.
- Download the latest version of Python (make sure to check the box that says "Add Python to PATH" during the installation).
- Verify the installation by opening a command prompt (Windows) or terminal (Mac, Linux) and typing `python --version`. This should return the version of Python you installed.

#### Setting Up the Development Environment:
There are many integrated development environments (IDEs) you can use for Python, but for beginners, IDLE (comes with Python installation) or Thonny are good options. As you get more advanced, you may want to switch to PyCharm or Visual Studio Code.

### 1.2 Understanding Python Syntax
Python is designed to be easy to understand and fun to use. Its syntax is simple and straightforward:

- Python uses indentation to define blocks of code instead of brackets or braces as in other programming languages.
- Statements in Python typically end with a new line. Python does, however, allow the use of the line continuation character (\) to denote that the line should continue.

### 1.3 Data Types: Strings, Numbers, and Booleans
Python has several data types. Here we will cover the most basic ones:

- **Strings**: Used for text, denoted by single (`'`) or double (`"`) quotes. Example: `my_string = "Hello, World!"`.
- **Numbers**: Python has two numeric types, integers and floats (decimals). Example: `my_int = 10`, `my_float = 10.5`.
- **Booleans**: Used for logical operations, can be either `True` or `False`.

### 1.4 Variables, Operators, and Expressions
Variables are containers for storing data. The equal sign (`=`) is used to assign values to variables. Operators are used to perform operations on variables and values. Python divides the operators in the following groups:
- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

### 1.5 Control Structures: If, Else, Elif
Python supports the usual logical conditions from mathematics:
- Equals: `a == b`
- Not Equals: `a != b`
- Less than: `a < b`
- Less than or equal to: `a <= b`
- Greater than: `a > b`
- Greater than or equal to: `a >= b`

These conditions can be used in several ways, most commonly in "if statements" and loops.

**If Statement**: An "if statement" is written by using the `if` keyword.

**Else Statement**: The `else` keyword catches anything which isn't caught by the preceding conditions.

**Elif Statement**: The `elif` keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

### 1.6 Mini-Project: Write a Python program to perform basic arithmetic operations.
This mini project will consolidate your understanding of the basics of Python. The goal is to create a program that takes two numbers as input and then allows the user to perform addition, subtraction, multiplication, or division on these numbers. This will require input/output, variables, operators, and control structures, thus reinforcing your understanding of these topics.

Let's break down the steps for this mini-project:
1. Prompt the user for two numbers and store these in variables.
2. Prompt the user for an operation (add, subtract, multiply, divide).
3. Use an if/elif/else structure to determine which operation to perform.
4. Perform the operation and print the result.

By the end of this chapter, you will have a basic understanding of Python, including how to write and execute Python programs, how to use different data types, and how to control the flow of your program with conditionals. This foundation will be built upon in the following chapters as you learn more advanced topics.