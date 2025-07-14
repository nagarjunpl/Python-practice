''' Write a Python program to generate a square matrix of size N × N, where each element at position (i, j) 
    is calculated using the formula: value = |i - j| + 1  '''


inp_int = int(input("enter the number of rows and columns : "))

for i in range(inp_int):
    for j in range(inp_int):
        value = abs(i - j) + 1    # Calculate the value as per the pattern: |i - j| + 1
        print(f"{value} ",end="")   # Print the value with a space, without moving to a new line
    print()   # Move to the next line after each row is printed