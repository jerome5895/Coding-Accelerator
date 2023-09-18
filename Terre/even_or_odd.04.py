import sys

# Function that try/except integer
def try_except(integer):
    try:
        integer = int(integer)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        sys.exit()
    except IndexError:
        print("There is not input.")
        sys.exit()
    return integer

# Function that displays if even or odd
def even_or_odd(integer):
    if integer % 2 == 0:
        print("even")
    else:
        print("odd")
    if integer < 0:
        print("negative")

# Function that manage if more than one integer
def len_integer():
    if len(sys.argv) != 2:
        print("Invalid input. Please provide only one integer.")
        sys.exit()

# Call function to verify only one integer
len_integer()

# Globales variables 
integer = try_except(sys.argv[1])

# Call function to know if even or odd and manage errors
even_or_odd(integer)