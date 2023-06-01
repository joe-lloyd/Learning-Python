## Chapter 5: Introduction to OOP (Object-Oriented Programming)

### 5.1 Classes and Objects
Classes and objects form the core of OOP. 

- **Class**: A class is like a blueprint for creating objects. It defines a set of attributes that will characterize any object that is instantiated from the class.

```python
class Car:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def start(self):
        print(f"The {self.color} {self.brand} is starting.")
```

- **Object**: An object is an instance of a class. An object has the structures and behavior defined in the class.

```python
my_car = Car("red", "Toyota")
my_car.start()  # Outputs: The red Toyota is starting.
```

### 5.2 Inheritance
Inheritance is a way of creating a new class using details of an existing class without modifying it. The newly formed class is called a derived (or child) class and the existing class is called the base (or parent) class.

```python
class Vehicle:
    def __init__(self, color):
        self.color = color

class Car(Vehicle):
    def __init__(self, color, brand):
        super().__init__(color)
        self.brand = brand
```

### 5.3 Encapsulation
Encapsulation refers to hiding the internal details of how an object works. In Python, we can use private attributes and methods to encapsulate class data.

- Private attributes are denoted by a leading underscore (`_`). 

- Private methods are also denoted by a leading underscore (`_`). 

These private members are not directly accessible from the objects of the class.

### 5.4 Polymorphism
Polymorphism allows us to define methods in the child class with the same name as defined in their parent class. A child class inherits all the methods from the parent class. However, it is possible to modify a method in a child class that it has inherited from the parent class. This is particularly useful in cases where the method inherited from the parent class doesn’t quite fit the child class.

### 5.5 Mini-Project: Write a simple class-based system to represent geometric shapes and their properties
The goal of this mini-project is to create a Python class-based system that can represent basic geometric shapes and their properties. This will allow you to practice defining classes, creating objects, and using inheritance.

Here's a breakdown of the mini-project:

1. Create a base class `Shape` with attributes common to all shapes and methods to calculate area and perimeter.

2. Create derived classes `Circle`, `Rectangle`, and `Triangle`, each with their unique attributes and methods.

3. Each derived class should override the base class methods for calculating area and perimeter.

4. Create objects of these classes and display their properties.

By the end of this chapter, you will understand the basic concepts of object-oriented programming and how to implement them in Python. These concepts are fundamental to writing organized, reusable, and easy-to-understand code.