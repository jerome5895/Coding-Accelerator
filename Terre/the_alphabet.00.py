# Function to return a string of the alphabet
def alphabet():
    alphabet_list = []
    # Get the alphabet
    for i in range(97, 123):
        alphabet_list.append(chr(i))
    return "".join(alphabet_list)

# Print out result
print(alphabet())