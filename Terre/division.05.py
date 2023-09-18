import sys

# Function that manages errors
def try_except(nbr1, nbr2):
    try:
        nbr1 = int(nbr1)
        nbr2 = int(nbr2)
    except ZeroDivisionError:
        print("Invalid input. One of your numbers is zero.")
        sys.exit()
    except ValueError:
        print("Invalid input. Please enter two integers.")
        sys.exit()
    except IndexError:
        print("Invalid input. One integer at least is missing")
        sys.exit()
    return nbr1, nbr2

# Function that returns result and remainder
def result_remainder(nbr1, nbr2):
    return nbr1 // nbr2, nbr1 % nbr2

# Function that returns if divider too big
def divider_size(nbr1, nbr2):
    if nbr2 > nbr1:
        print("Invalid input. Your divider is bigger than your dividend.")
        sys.exit()

# Unpack the tuple returned by try_except
try:
    nbr1, nbr2 = try_except(sys.argv[1], sys.argv[2])
except IndexError:
    print("Invalid input. One integer at least is missing.")
    sys.exit()

# Call function to print out result and remainder expected
divider_size(nbr1, nbr2)
result, remainder = result_remainder(nbr1, nbr2)
print(f"Result: {result}")
print(f"Remainder: {remainder}")