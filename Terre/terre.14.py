import sys

# Function to manage errors
def try_except():
    if len(sys.argv) < 3:
        print("Invalid input. Please provide at least two integers.")
        sys.exit()
    try:
        integers = [int(integer) for integer in sys.argv[1:]]
        return integers
    except ValueError:
        print("Invalid input. Please enter a list of integers.")
        sys.exit()
    
# Call function to manage errors
integers = try_except()

# Function to know if list of integers is sorted
def if_integers_sorted(integers):
    sorted = True
    for i in range(len(integers) - 1):
        if integers[i] > integers[i+1]:
            sorted = False
            break
    return sorted

is_sorted = if_integers_sorted(integers)

# Print out the exit of function `sort_integers`
if is_sorted:
    print("Your list is sorted!")
else:
    print("Your list is not sorted!")