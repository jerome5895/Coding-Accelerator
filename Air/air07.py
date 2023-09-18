import sys

# Function to manage index and value errors
def try_except():
    if len(sys.argv) < 4:
        print("Invalid input. Please provide at least two numbers with an additional element.")
        sys.exit()
    try:
        array = [int(array) for array in sys.argv[1:-1]]
        new_element = [int(new_element) for new_element in sys.argv[-1:]]
    except ValueError:
        print("Invalid input. Please provide only numbers.")
        sys.exit()
    return array, new_element

# Function to add and sort the new element in the array
def selection_sort(array, new_element):
    new_array = array + new_element
    n = len(new_array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if new_array[j] < new_array[min_index]:
                min_index = j
        new_array[i], new_array[min_index] = new_array[min_index], new_array[i]
    return new_array

# Resolution
array, new_element = try_except()
new_array = selection_sort(array, new_element)

# Print out result
print(new_array)