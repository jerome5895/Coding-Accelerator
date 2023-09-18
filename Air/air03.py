import sys

# Function to find any alone argument
def find_alone(array):
    counts = {}
    count = 0
    for i in range(0, len(array)):
        firstword = array[i]
        for i in range(0, len(array)):
            secondword = array[i]
            if firstword == secondword:
                count += 1
        counts[firstword] = count
        if count == 1:
            print(firstword)
        count = 0
    return array

# Function to manage index errors
def if_errors(array):
    if len(array) < 3:
        print("Invalid input. Please provide at least three arguments.")
        sys.exit()
    return array

# Convert globales variables
array = sys.argv[1:]

# Resolution
if_errors(array)
new_array = find_alone(array)

# Print out result
print(new_array)