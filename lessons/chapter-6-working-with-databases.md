## Chapter 6: Working with Databases

### 6.1 Introduction to SQLite
SQLite is a software library that provides a relational database management system. The unique aspect of SQLite is that it's serverless and self-contained. SQLite stores the entire database (definitions, tables, indices, and the data itself) as a single cross-platform file on a host machine.

### 6.2 CRUD Operations
CRUD stands for Create, Read, Update, and Delete, which are the four basic functions that models should be able to do, at most.

- **Create**: Inserting data into tables.
- **Read**: Selecting data from a table which returns a result set.
- **Update**: Updating existing data within a table.
- **Delete**: Removing data from a table.

### 6.3 Python's SQLite Module
Python's `sqlite3` module is a straightforward and easy-to-use interface for interacting with SQLite databases. It is included in Python by default.

Here's how you can create a connection with a SQLite database:
```python
import sqlite3
conn = sqlite3.connect('my_database.db')
```
Once the connection is created, you can then create a Cursor object and call its execute() method to perform SQL commands.

```python
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2020-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# close the connection if we are done with it.
conn.close()
```

### 6.4 Relationships Between Tables
Relational databases are designed to model relationships between tables. The main types of table relationships are:

- **One-to-One**: One record in a table is associated with one and only one record in another table.
- **One-to-Many**: One record in a table can be associated with one or more records in another table.
- **Many-to-Many**: Multiple records in a table can be associated with multiple records in another table.

### 6.5 Mini-Project: Write a program to manage a SQLite database of books
In this mini-project, you will create a SQLite database to store information about books. The database will have a single table named `books` with columns for `title`, `author`, `genre`, and `year`.

You should write a Python program that allows the user to perform CRUD operations on the database:

- **Create**: Add a new book to the database.
- **Read**: Retrieve information about a book from the database.
- **Update**: Update information about a book in the database.
- **Delete**: Remove a book from the database.

By the end of this chapter, you should be comfortable working with databases in Python, and you will understand how to create, read, update, and delete data from a SQLite database.