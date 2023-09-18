import sys

# Function to manage errors
def try_except(nbr):
    try:
        nbr = int(nbr)
    except ValueError:
        print("Please enter an integer.")
        sys.exit()
    except IndexError:
        print("Invalid input. No provided number.")
        sys.exit()
    return nbr

# Function to check length of input
def length_argument():
    if len(sys.argv) > 2:
        print("Invalid input. Please provide only one integer.")
        sys.exit()

# Function to displays if even or odd
def even_or_odd(nbr):
    if nbr > 1:
        for i in range(2, int(nbr/2)+1):
            if (nbr % i) == 0:
                print("It is not a prime number.")
                break
        else:
            print("It is a prime number.")
    else:
        print("It is not a prime number.")

# Unpack the tuple returned by try_except
try:
    nbr = try_except(sys.argv[1])
except IndexError:
    print("Invalid input. No provided argument.")
    sys.exit()

# Call function to check length of input and print out even or odd
length_argument()
even_or_odd(nbr)