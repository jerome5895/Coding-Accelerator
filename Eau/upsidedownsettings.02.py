import sys

# Export arguments
arguments = sys.argv[1:]

# Function to reverse all arguments
def reverse_arg(arguments):
    reversed_arguments = ""
    for reverse in arguments:
        reversed_arguments = reverse + reversed_arguments
    return reversed_arguments

# Function to manage errors
def if_errors():
    if len(arguments) < 1:
        print("Invalid input. Please restart the program and provide at least two arguments if you want result.")
        sys.exit()
    return arguments

# Globales variables
arguments = if_errors()
reversed_arguments = reverse_arg(arguments)

# Print out
print(reversed_arguments)