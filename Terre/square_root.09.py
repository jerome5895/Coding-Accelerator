import sys

# Function to manage errors
def try_except(nbr):
    try:
        nbr = int(nbr)
    except ValueError:
        print("Invalid input. Please provide only integer.")
        sys.exit()
    except IndexError:
        print("Invalid input. No number provided.")
        sys.exit()
    return nbr

# Function to calcul the square root
def square_root(nbr):
    return int(nbr) ** 0.5

# Function to verify if negative exponent
def verify_negative_number(nbr):
    if int(nbr) < 0:
        print("Invalid input. Negative number.")
        sys.exit()

# Unpack the tuple receved by the try_except
try:
    nbr = sys.argv[1]
except IndexError:
    print("Invalid input. no number provided.")
    sys.exit()

# Function to check if more than one argument
def if_multi_nbr(length):
    if length > 2:
        print("Invalid input, please provide only one integer.")
        sys.exit()

# Call function to verify length, try_except, negative number and to print out 
length = len(sys.argv)
try_except(nbr)
if_multi_nbr(length)
verify_negative_number(nbr)
print(f"The square root is: {square_root(nbr)}")