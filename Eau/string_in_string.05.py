import sys

# Function to spot if substring in string
def if_sub_in_str():
    if substring in str:
        print("True")
    else:
        print("False")
        sys.exit()
    return True, False

# Function to manage Indexerrors
def try_except():
    try:
        str = sys.argv[1]
        substring = sys.argv[2]
    except IndexError:
        print("Invalid input. Please provide one string and one substring.")
        sys.exit()
    return str, substring

# Convert to globales variables
str, substring = try_except()

# Print out if True or False
if_sub_in_str()
