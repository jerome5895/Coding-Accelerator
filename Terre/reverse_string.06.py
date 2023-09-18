import sys

# Function to manage errors
def try_except():
    try:
        string = sys.argv[1]
        if len(string) < 2:
            raise ValueError
    except (IndexError, ValueError):
        print("Invalid input. Please provide at least two characters.")
        sys.exit(1)
    return string

# Function to reverse string
def argument_reverse(string):
    reversed_string = ""
    for substring in string:
        reversed_string = substring + reversed_string
    return reversed_string

# Assign variables and print out
string = try_except()
reversed_string = argument_reverse(string)
print(reversed_string)
