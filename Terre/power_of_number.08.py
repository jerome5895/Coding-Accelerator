import sys

# Function to manage errors
def try_except(nbr1, nbr2):
    try:
        nbr1 = int(nbr1)
        nbr2 = int(nbr2)
    except ValueError:
        print("Invalid input. Please provide only integers.")
        sys.exit()
    except IndexError:
        print("Invalid input. One integer at lest is missing.")
        sys.exit()
    return nbr1, nbr2

# Function to calcul power
def power(nbr1, nbr2):
    return nbr1 ** nbr2

# Unpack the tuple returned by the try_except
try:
    nbr1, nbr2 = try_except(sys.argv[1], sys.argv[2])
except IndexError:
    print("Invalid input. One integer at least is missing.")
    sys.exit()

# Function that checks if exponent is negative
def verify_negative_exponent(nbr2):
    if int(nbr2) < 0:
        print("Invalid input. Negative number.")
        sys.exit()

# Call function to checks exponent and print out result
verify_negative_exponent(nbr2)
result = power(nbr1, nbr2)
print(f"The result is: {result}")
