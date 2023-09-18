import sys

# Function to display if string is not in array
def if_string(array, string):
    list_not = ""
    for arr in array:
        if string not in arr:
            list_not += arr + ", "
    return list_not

# Function to manage index errors
def index_errors(array, string):
    if len(array) < 1 or len(string) > 1:
        print("Invalid input. Please enter at least one string and one comparison character.")
        sys.exit()
    return array, string

# Convert globales variables
array = sys.argv[1:]
string = sys.argv[-1]

# Resolution
index_errors(array, string)
new_array = if_string(array, string)

# Print out result
print(new_array)