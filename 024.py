#  given two integers A and B, write a program to add these two numbers and output the sum.

# Read the number of test cases from the user
t = int(input("Enter number of test cases: "))

# Loop through each test case
for i in range(t):
    # Read two integers from the user for each test case
    a, b = map(int, input(f"Enter two numbers for test case {i+1} (separated by space): ").split())

    # Calculate the sum of the two integers
    result = a + b

    # Print the result
    print("Sum:", result)
