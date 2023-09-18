import sys

# Function that returns alphabet from given letter in the prompt
def alphabet_from_():
    letter_from = ord(sys.argv[1])
    alphabet = range((letter_from), (123))
    for letter in alphabet:
        print(chr(letter), end="")
    print(("\n"), end="")

# Call function
alphabet_from_()