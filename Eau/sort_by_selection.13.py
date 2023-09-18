import sys

# Function to sort a list of numbers by "selection_sort method"
def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
                array[i], array[min_index] = array[min_index], array[i]
    return array

# Function to manage Value and Index errors
def try_except():
    if len(sys.argv) < 3:
        print("Invalid input. Please provide at least two numbers.")
        sys.exit()
    try:
        array = [int(array) for array in sys.argv[1:]]
    except ValueError:
        print("Invalid input. Please provide only numbers.")
        sys.exit()
    return array

# Function to print out without []
def without_brackets():
    for i in range(len(array)):
        print((array[i]), end=" ")
    print()

# Convert globales variables and print out
array = try_except()
selection_sort(array)
array = without_brackets()