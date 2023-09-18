import sys

# Function to have N Fibonacci from index given
def i_fibo(n):
    if n < 2:
        print("-1")
        sys.exit()
    Upp = 0
    Up = 1
    for i in range(n-1):
        U = Upp + Up
        Upp = Up
        Up = U
    return U

# Function to manage errors of argument
def try_except():
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Invalid input. Please provide only numbers.")
        sys.exit()
    return n

# Convert globales variables
n = try_except()
U = i_fibo(n)

# Print out Fibonacci
print(U)
