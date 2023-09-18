import sys

# Function to generate list difference of numbers between nbr1 and nbr2
def list_difference(nbr1, nbr2):
    suite = ""
    if nbr1 < nbr2:
        while nbr1 != nbr2:
            suite += str(nbr1) + " "
            nbr1 += 1
    else:
        if nbr1 > nbr2:
            while nbr1 != nbr2:
                suite += str(nbr2) + " "
                nbr2 += 1
        else:
            print("The two integers are equal.")
    return suite

# Function to manage Value and Index Errors
def try_except():
    try:
        nbr1 = int(sys.argv[1])
        nbr2 = int(sys.argv[2])
    except ValueError:
        print("Invalid input. Please provide two integers.")
        sys.exit()
    except IndexError:
        print("Invalid input. One integer at least is missing.")
        sys.exit()
    return nbr1, nbr2

# Globales variables
nbr1, nbr2 = try_except()
suite = list_difference(nbr1, nbr2)

# Print out list
print(suite)