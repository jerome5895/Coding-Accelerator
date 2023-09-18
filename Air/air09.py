import sys

# Function to move first argument in last index
def to_left(argument):
    new_string = []
    changed_word = []
    for index, word in enumerate(argument):
        if index != 0:
            new_string.append(word)
        else:
            changed_word = word
    new_string.append(changed_word)
    return new_string

# Function to manage index and value errors
def try_except(argument):
    if len(sys.argv) < 3:
        print("Invalid input. Please provide at least two arguments.")
        sys.exit()
    try:
        for value in argument:
            if value.isdigit():
                raise ValueError
    except ValueError:
        print("Invalid input. Please provide only string, no integers.")
        sys.exit()
    return argument

# Function to print out without bracket and ","
def without_bracket(new_string):
    for i in range(len(new_string)):
        print(new_string[i], end=" ")
    print()

# Convert globales variables
argument = sys.argv[1:]
try_except(argument)
new_string = to_left(argument)

# Print out result
without_bracket(new_string)