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

# Function to manage argument errors
def errors(string_to_cut):
    if len(sys.argv) != 2:
        print("Invalid input. Please provide one argument.")
        sys.exit()

# Function to print out without []
def without_brackets(words):
    for i in range(len(words)):
        print((words[i]), end='\n')
    print()

# Convert globales variables
string_to_cut = sys.argv[1]
separators = [' ', '\t', '\n']

# Resolution
errors(string_to_cut)
words = separation(string_to_cut, separators)

# Print out result
without_brackets(words)