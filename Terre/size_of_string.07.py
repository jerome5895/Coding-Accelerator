import sys

# Function to manage errors
def try_except(argument):
    try:
        argument = sys.argv[1]
    except IndexError:
        print("There is not any input.")
        sys.exit()
    return argument

argument = try_except(sys.argv)

# Function to check if argument is only numbers
def is_only_numbers(argument):
    return argument.isdigit()

# Function to have the length of the argument
def length_argument(argument):
    length = 0
    for char in str(argument):
        length = length + 1
    return str(length)

# Checks if only numbers or more than one argument
if is_only_numbers(argument):
    print("Invalid input. Please do not enter only numbers.")
    sys.exit()
if len(sys.argv) > 2:
    print("Invalid input. Please enter only 'one argument'.")
    sys.exit()

# Call function to check errors and function to print the length
length = try_except(argument)
print(length_argument(argument))