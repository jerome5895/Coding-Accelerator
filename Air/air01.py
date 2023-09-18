import sys

# Function to separate argument
def separation(string_to_cut, separators):
    words = []
    current_word = ""
    for char in string_to_cut:
        if char in separators:
            if current_word:
                words.append(current_word)
                current_word = ''    
        else:
            current_word += char
    if current_word:
        words.append(current_word)
    return words

# Function to separate in terms of argument 2
def without_sep(words, new_separators):
    array = []
    found_separator = False
    for word in words:
        if word == new_separators:
            found_separator = True
            break
        array.append(word)
    if found_separator:
        words = words[len(array)+1:]
    else:
        words = []
    return array, words

# Function to print out without []
def without_brackets(array):
    for i in range(len(array)):
        print((array[i]), end=' ')
    print()

# Convert globales variables
string_to_cut = sys.argv[1]
separators = [' ', '\t', '\n']
new_separators = sys.argv[2]

# Resolution
words = separation(string_to_cut, separators)
array = without_sep(words, new_separators)

# Print out result
without_brackets(array)