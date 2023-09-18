import sys

# Function to sort a list by ASCII order
def selection_sort(array):
    n = len(array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

# Function to print out without []
def chr_without_brackets(array):
    for l in range(len(array)):
        print(array[l], end=" ")
    print()

# Function to manage IndexError
def try_except():
    if len(sys.argv) < 3:
        print("Invalid input. Please provide at least two letters or two words or two numbers.")
        sys.exit()
    return array

# Convert globales variables
array = sys.argv[1:]
array = try_except()

# Call functions and print out
selection_sort(array)
chr_without_brackets(array)