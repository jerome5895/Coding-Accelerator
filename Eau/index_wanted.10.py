import sys

# Function to check if last word is in array
def if_in_array(array, last_word):
    index = -1
    for i in array:
        index += 1
        if i == last_word:
            print(index)
            break
    if last_word not in array:
        print("-1")

# Function to manage IndexError
def IndexError():
    if len(sys.argv) < 3:
        print("Invalid input. Please provide at least two arguments.")
        sys.exit()

# Convert globales variables
array = sys.argv[1:-2]
last_word = sys.argv[-1]
IndexError()

# Print out result
if_in_array(array, last_word)