# Function to generate first and second number, finaly make all combinations with its
def valid_combinations():
    valid_comb = ""
    for i in range(10):
        for j in range(10):
            first_comb = str(i) + str(j)
            for k in range(10):
                for l in range(10):
                    second_comb = str(k) + str(l)
                    if first_comb < second_comb and first_comb != second_comb:
                        valid_comb += f"{str(first_comb)} {str(second_comb)}, "
                        
    print(valid_comb)

# Call function to print out 
valid_combinations()    