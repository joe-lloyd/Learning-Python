def get_file_name():
    file_name = input("Please enter the file name: ")
    return file_name


def choose_file_operation():
    print("0 - Main Menu")
    print("1 - Read the file")
    print("2 - Write to the file")
    print("3 - Append to the file")
    print("4 - Exit")
    valid_choices = ['0', '1', '2', '3', '4']
    choice = input("Please enter a valid choice: ")
    while choice not in valid_choices:
        choice = input("Please enter a valid choice: ")
    return choice


def read_file(file_name):
    try:
        file = open(file_name, 'r')
        for line in file:
            print(line, end='')
        file.close()
    except FileNotFoundError:
        print("File not found")


def write_to_file(file_name):
    try:
        file = open(file_name, 'w')
        file.write(input("Please enter the text to write to the file: "))
        file.close()
    except FileNotFoundError:
        print("File not found")


def append_to_file(file_name):
    try:
        file = open(file_name, 'a')
        file.write(input("Please enter the text to append to the file: "))
        file.close()
    except FileNotFoundError:
        print("File not found")


# Main function for text file management
def main():
    file_name = get_file_name()
    choice = choose_file_operation()
    while choice != '4':
        if choice == '0':
            choice = choose_file_operation()
        elif choice == '1':
            read_file(file_name)
            choice = choose_file_operation()
        elif choice == '2':
            write_to_file(file_name)
            choice = choose_file_operation()
        elif choice == '3':
            append_to_file(file_name)
            choice = choose_file_operation()


main()
