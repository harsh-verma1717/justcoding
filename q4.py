# Function to print Fibonacci sequence up to a given number
def print_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print()  # For a new line after printing the sequence

# Function to print factorials in the format: "Factorial of i is <value>"
def print_factorials(n):
    i = 1
    factorial = 1
    while i <= n:
        factorial *= i
        print(f"Factorial of {i} is {factorial}")
        i += 1

# Read number from the user
num = int(input("Enter a number: "))

# Logic based on the value of the number
if num > 0:
    print_fibonacci(num)
elif num < 0:
    print_factorials(abs(num))
else:
    print("No computation required.")
