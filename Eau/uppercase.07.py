import sys

# Function to separate words
def separate():
    argument = sys.argv[1]
    words = []
    current_word = ""
    for char in argument:
        if char in [' ', '\t', '\n']:
            if current_word:
                words.append(current_word)
                current_word = ''
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    return words

# Function to capitalize first letter of every word
def capitalize_first():
    capitalized_words = []
    for word in words:
        capitalized_word = ''
        for i, char in enumerate(word):
            if i == 0:
                if ord(char) >= 48 and ord(char) <= 57:
                    print("Invalid input. Please do not provide any integers.")
                    sys.exit()
                if ord(char) >= 97 and ord(char) <= 122:
                    capitalized_word += chr(ord(char) - 32)
                else:
                    capitalized_word += char
            else:
                capitalized_word += char.lower()
        capitalized_words.append(capitalized_word)
    return capitalized_words

# Function to concatenate every words
def concatenate():
    output_str = ''
    for i, word in enumerate(capitalized_words):
        if i == 0:
            output_str += word
        else:
            output_str += ' ' + word
    return output_str

# Convert globales variables
words = separate()
capitalized_words = capitalize_first()
output_str = concatenate()

# Print out the argument with every first letter capitalized
print(output_str)