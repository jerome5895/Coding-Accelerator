# Edit my notes
my_sentence = "J'ai terminé l'épreuve de la Terre. C'était souvent difficile:("
my_green_points = ["Table ASCII", "Syntaxe", "Conditions", "Github"]
my_less_green_points = ["Loop", "More developed algorithmics", "New functions"]

# Convert notes to variables
sentence = my_sentence
right = my_green_points
not_right = my_less_green_points

# Function to print out my notes
def print_out_feelings():
    print(f"{sentence}") 
    print(f"Mes facilités: {right[:]}")
    print(f"Mes difficultés: {not_right[:]}")

# Call function to print out my notes
print_out_feelings()