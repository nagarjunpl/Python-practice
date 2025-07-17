# This code prints a pyramid pattern of numbers.

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):  # Loop through each row
    print("  " * (n - i), end="")    # Print leading spaces for alignment

    for j in range(1, i + 1):   # Print numbers in ascending order
        print(j, end=" ")      # Print numbers in the current row

    for j in range(i - 1, 0, -1):     # Print numbers in descending order
        print(j, end=" ")        # Print numbers in the current row

    print("")     # Move to the next line after each row is printed