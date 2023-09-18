import sys

# Function to displays next first-number
def next_nbr_first(nbr):
    all_first = []
    for nbr_first in range(nbr, nbr+100):
        if nbr_first < 2:
            print("-1")
            sys.exit()
        est_premier = True
        for diviseur in range(2, nbr_first//2+1):
            if nbr_first % diviseur == 0:
                est_premier = False
                break
        if est_premier:
            all_first.append(nbr_first)
    print(all_first[0])

# Function to manage errors
def try_except():
    try:
        nbr = int(sys.argv[1])
    except ValueError:
        print("-1")
        sys.exit()
    return nbr

# Convert globales variables
nbr = try_except()

# Print out next first-number
next_nbr_first(nbr)