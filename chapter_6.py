import sqlite3

connection = sqlite3.connect('chapter_6.db')


def create_books_table():
    try:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE books
                        (title text, author text, genre text, year integer)''')
        connection.commit()
        print("Table created successfully")
    except sqlite3.OperationalError:
        print("Table already exists")


def seed_books_table():
    try:
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO books VALUES ("The Giver", "Lois Lowry", "young adult", 1993)''')
        cursor.execute('''INSERT INTO books VALUES ("The Handmaid's Tale", "Margaret Atwood", "dystopian", 1985)''')
        cursor.execute('''INSERT INTO books VALUES ("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 
        "comedy", 1979)''')
        connection.commit()
        print("Table seeded successfully")
    except sqlite3.OperationalError:
        print("Unable to seed table")


def create_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    genre = input("Enter the genre of the book: ")
    year = input("Enter the year the book was published: ")
    try:
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO books VALUES (?, ?, ?, ?)''', (title, author, genre, year))
        connection.commit()
        print("Book added successfully")
    except sqlite3.OperationalError:
        print("Unable to add book")


def read_book():
    title = input("Enter the title of the book: ")
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM books WHERE title = ?''', (title,))
        book = cursor.fetchone()
        print(book)
    except sqlite3.OperationalError:
        print("Unable to retrieve book")


def update_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    genre = input("Enter the genre of the book: ")
    year = input("Enter the year the book was published: ")
    try:
        cursor = connection.cursor()
        cursor.execute('''UPDATE books SET author = ?, genre = ?, year = ? WHERE title = ?''',
                       (author, genre, year, title))
        connection.commit()
        print("Book updated successfully")
    except sqlite3.OperationalError:
        print("Unable to update book")


def delete_book():
    title = input("Enter the title of the book: ")
    try:
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM books WHERE title = ?''', (title,))
        connection.commit()
        print("Book deleted successfully")
    except sqlite3.OperationalError:
        print("Unable to delete book")


def read_all_books_titles():
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT title FROM books''')
        books = cursor.fetchall()
        print(books)
    except sqlite3.OperationalError:
        print("Unable to retrieve books")


def select_crud_action():
    print("1. Create a book")
    print("2. Read a book")
    print("3. Read all book")
    print("4. Update a book")
    print("5. Delete a book")
    print("6. Exit")
    return input("What would you like to do? ")


def main():
    while True:
        action = select_crud_action()
        if action == "1":
            create_book()
        elif action == "2":
            read_book()
        elif action == "3":
            read_all_books_titles()
        elif action == "4":
            update_book()
        elif action == "5":
            delete_book()
        elif action == "6":
            break
        else:
            print("Invalid input")
    connection.close()


main()
