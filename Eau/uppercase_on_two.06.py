import sys

# Function to convert string to "StRiNg-format"
def UP_lowcase():
    new_string = ""
    for n in range(len(string)):
        if ord(string[n]) >= 48 and ord(string[n]) <= 57:
            print("Invalid input. Please don't provide any integer.")
            sys.exit()
        if n % 2 == 0:
            if ord(string[n]) >= 97:
                new_string += chr(ord(string[n]) - 32)
            else:
                new_string += string[n]
        else:
            new_string += string[n]
    return new_string

# Function to manage IndexErrors
def try_except():
    try:
        string = sys.argv[1]
    except IndexError:
        print("Invalid input. No string provided.")
        sys.exit()
    return string

# Convert globales variables
string = try_except()
Good_string = UP_lowcase() 

# Print out input in "StRiNg-format"
print(Good_string)