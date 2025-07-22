# Write a Python program to print multiplication tables from a given starting number to an ending number.

# Take input from the user for the starting table number
a = int(input("Enter which table to start from: "))

# Take input from the user for the ending table number
b = int(input("Enter which table to end at: "))

# Loop through each number from a to b (inclusive)
for i in range(a, b + 1):
    
    # Loop through numbers 1 to 10 for each table
    for j in range(1, 11):
        
        # Print the multiplication result in formatted form
        print(f"{i} x {j} = {i * j}")
