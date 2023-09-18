import sys

# Function to generate string without two consecutive characters
def if_repet(array):
    n = len(array)
    result = array[0]
    for i in range(1, n):
        if array[i] != array[i-1]:
            result += array[i]
    return result

# Function to manage index errors
def try_except():
    try:
        array = sys.argv[1]
    except IndexError:
        print("Invalid input. Please provide one argument.")
        sys.exit()
    return array

# Convert globales variables
array = try_except()
result = if_repet(array)

# Print out result
print(result)