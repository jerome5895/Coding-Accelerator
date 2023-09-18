import sys

# Function to sort the integers
def selection_sort(integers):
    n = len(integers)
    for i in range(n - 1):
        min_index = i
        for j in range(i+1, n):
            if integers[j] < integers[min_index]:
                min_index = j
                integers[i], integers[min_index] = integers[min_index], integers[i]
    return integers

# Function to stock the absolute minimum difference
def diff_list():
    sorted_integers = selection_sort(integers)
    min_diff = float('inf')
    n = len(sorted_integers)
    for i in range(n - 1):
        diff = abs(sorted_integers[i] - sorted_integers[i + 1])
        if diff < min_diff:
            min_diff = diff
    return min_diff

# Function to manage errors argument
def try_except():
    if len(sys.argv) < 3:
        print("Invalid input. Please enter at least two integers.")
        sys.exit()
    try:
        integers = [int(integers) for integers in sys.argv[1:]]
    except ValueError:
        print("Invalid input. Please enter only integers.")
        sys.exit()
    return integers

# Convert global variables
integers = try_except()
min_diff = diff_list()

# Print out result
print(min_diff)