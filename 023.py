# Write a Python program to calculate the factorial of a given number.

# Take an integer input from the user
num = int(input())

# Initialize factorial result to 1
fact = 1

# Check if the number is 0
if num == 0:
    fact = 1  # Factorial of 0 is 1
else:
    # Calculate factorial using a while loop
    while num > 0:
        fact = fact * num  # Multiply current number with result
        num -= 1           # Decrement the number by 1

# Print the factorial result
print(fact)
