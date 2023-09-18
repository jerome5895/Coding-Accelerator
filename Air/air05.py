import sys

# Function to manage value errors
def value_error():
    try:
        integers = [int(integers) for integers in sys.argv[1:-1]]
        operation = sys.argv[-1][0]
        nbr = sys.argv[-1][1:]
    except ValueError:
        print("Invalid input. Please provide only integer to the list, not any character.")
        sys.exit()
    return integers, operation, nbr

# Function to manage index errors
def index_error(operation):
    if len(sys.argv) < 2 or operation not in ["+", "-"] or len(nbr) < 1:
        print("Invalid input. Please provide at least one integers. Then, provide one sum or substraction operation.")
        sys.exit()
        
# Function to calculate operation "+" in any integers of a list
def add(integers, nbr):
    for i in range(len(integers)):
        if operation == "+":
            integers[i] += int(nbr)
            print(integers[i])
    return integers, nbr

# Function to calculate operation "-" in any integers of a list
def sub(integers, nbr):
    for i in range(len(integers)):
        if operation == "-":
            integers[i] -= int(nbr)
            print(integers[i])
    return integers, nbr

# Resolution
integers, operation, nbr = value_error()
index_error(operation)

# Print out result
add(integers, nbr)
sub(integers, nbr)