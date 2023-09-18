import sys
import os

# Function to manage index error
def index_error():
    if len(sys.argv) < 2:
        print("Invalid input. Usage: python " + sys.argv[0] + " FILENAME")
        sys.exit()

# Function to read file in argument
def read_file():
    try:
        with open(filename, 'r') as file:
            data = file.read()    
    except IOError:
        print("Error reading file. Please verify the filename.")
        sys.exit()
    return filename, data

# Call function
index_error()

# Resolution
filename = sys.argv[1]
filename, data = read_file()

# Print out result
print(data)