import sys

# Function to separate argument by string 
def separate(argument):
    separator = "fusion"
    if separator in argument:
        index = argument.index(separator)
        array1 = argument[:index]
        array2 = argument[index+1:]
    else:
        print("Invalid input. No 'fusion' word provided.")
        sys.exit()
    return array1, array2

# Function to sort and concatenate two arrays
def sorted_fusion(array1, array2):
    new_array = array1 + array2
    n = len(new_array)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if new_array[j] < new_array[min_index]:
                min_index = j
        new_array[i], new_array[min_index] = new_array[min_index], new_array[i]
    return new_array

# Function to manage index errors
def index_error(array1, array2):
    try:
        if len(array1) == 0 or len(array2) == 0:
            raise IndexError
    except IndexError:
        print("Invalid input. Please provide numbers before and after 'fusion'.")
        sys.exit()

# Function to manage value errors
def value_error(array1, array2):
    try:
        for value in array1 + array2:
            if not value.isdigit():
                raise ValueError
    except ValueError:
        print("Invalid input. Please provide only numbers before and after 'fusion'.")
        sys.exit()

# Function to print out without [] and ''
def without_brackets(new_array):
    for i in range(len(new_array)):
        print(new_array[i], end=" ")
    print()

# Convert globales variables
argument = sys.argv[1:]

# Resolution
array1, array2 = separate(argument)
index_error(array1, array2)
value_error(array1, array2)
new_array = sorted_fusion(array1, array2)

# Print out result
without_brackets(new_array)