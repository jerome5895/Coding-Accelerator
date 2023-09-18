import sys

# Function to manage errors
def try_except():
    if len(sys.argv) != 4:
        print("Invalid input. One integer at least is missing.")
        sys.exit()
    nbr1, nbr2, nbr3 = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        nbr1 = int(nbr1)
        nbr2 = int(nbr2)
        nbr3 = int(nbr3)
    except ValueError:
        print("Invalid input. Please provide three integers.")
        sys.exit()
    return nbr1, nbr2, nbr3

# Call function try_except
nbr1, nbr2, nbr3 = try_except()

# Function to find the middle number
def find_middle_nbr():
    if nbr1 == nbr2 and nbr1 == nbr3:
        print("The three integers are equal.")
        sys.exit()
    if nbr1 < nbr2 and nbr1 > nbr3 or nbr1 > nbr2 and nbr1 < nbr3:
        print(nbr1)
    elif nbr2 < nbr1 and nbr2 > nbr3 or nbr2 > nbr1 and nbr2 < nbr3:
        print(nbr2)
    else:
        print(nbr3)
    
# Call function to print out the middle number
find_middle_nbr()