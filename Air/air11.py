import sys

# Function to manage index error
def try_except():
    try:
        character = int(sys.argv[1])
        floors = int(sys.argv[2])
    except IndexError:
        print("Invalid input. Please provide one number and one number of floors.")
        sys.exit()
    except ValueError:
        print("Invalid input. Please provide only numbers.")
        sys.exit()
    return character, floors

# Function to display a pyramid
def pyramid(character, floors):
    l = floors
    for i in range(1, l+1):
        for j in range(1, l-i+1):
            print(" ", end="")
        for j in range(1, 2*i-1+1):
            print(character, end="")
        print()

# Call function
character, floors = try_except() 

# Print out result
pyramid(character, floors)