# Empty list to store valid combinations
valid_combinations = []

# Function to generate all combination and store validate combinations
def validate_combinations():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if i <= j <= k and len(set(str(i) + str(j) + str(k))) == 3:
                    valid_combinations = (str(i) + str(j) + str(k))
                    print(valid_combinations, end=",")
    print(("\n"), end="")

# Call function to print valid combinations
validate_combinations()