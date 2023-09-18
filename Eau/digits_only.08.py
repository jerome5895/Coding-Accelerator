import sys

# Function to verify if only integers
def if_all_integers():
    not_integer = ""
    integer = ""
    for char in argument:
        if ord(char) >= 48 and ord(char) <= 57:
            integer += char
        else:
            not_integer += char

    if len(not_integer) != 0:
        print("False.")
    else:
        print("True.")
    return argument

# Function to manage IndexError
def try_except():
    try:
        argument = sys.argv[1]
    except IndexError:
        print("Invalid input. Please provide at least one character.")
        sys.exit()
    return argument

# Globales variables
argument = try_except()

# Print out result
if_all_integers()