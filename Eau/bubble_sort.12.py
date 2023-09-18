import sys

# Function to sort a list without tri à bulle method
def tri_a_bulle(array):
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

# Function to manage Index and Value errors
def try_except():
    if len(sys.argv) < 3:
        print("Invalid input. Please enter at least two numbers.")
        sys.exit()
    try:
        array = [int(array) for array in sys.argv[1:]]
    except ValueError:
        print("Invalid input. Please enter only numbers.")
        sys.exit()
    return array

# Function to print without []
def without_brackets(array):
    for i in range(len(array)):
        print((array[i]), end=" ")
    print()

# Convert globales variables
array = try_except()

# Call function and print out result
tri_a_bulle(array)
without_brackets(array)