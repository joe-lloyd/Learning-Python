# Function to prompt the user for 2 numbers and store the variables
def get_numbers():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    return num1, num2


# Function to prompt the user for an operation (add, subtract, multiply, divide)
def get_operation():
    operation = input("Enter the operation (add, subtract, multiply, divide): ")
    return operation


# Function using if, elif, else to perform the operation on the 2 numbers
def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2
    else:
        return "Invalid operation"


# Function to print the result
def print_result(result):
    print("The result is: {0}".format(str(result)))


# Main function
def main():
    num1, num2 = get_numbers()
    operation = get_operation()
    result = calculate(num1, num2, operation)
    print_result(result)


main()
