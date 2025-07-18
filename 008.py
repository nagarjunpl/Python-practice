# Write a Python program to print a plus (+) shape pattern using stars (*) for a given number


n = int(input("Enter n value: "))

for i in range(n):     # of rows (n must be odd for a symmetric plus shape)
    for j in range(n):     # Loop through each row and column
        if i == n // 2 or j == n // 2:     # Check if it's the middle row or column
            print("*", end="  ")        # Print a star for the middle row or column
        else:
            print(" ", end="  ")       # Print a space for other positions
    print()
