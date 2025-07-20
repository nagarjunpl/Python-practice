# Write a program that takes an integer and prints "Weird" or "Not Weird" based on the conditions:

# Take integer input from the user and remove any leading/trailing spaces
n = int(input().strip())

# Check if the number is odd
if n % 2 != 0:
    print("Weird")  # Print "Weird" if the number is odd

else:
    # If number is even and in the range 2 to 5 (inclusive), or greater than 20
    if (n >= 2 and n <= 5) or n > 20:
        print("Not Weird")  # Print "Not Weird"
    # If number is even and in the range 6 to 20 (inclusive)
    elif (n >= 6 and n <= 20):
        print("Weird")  # Print "Weird"
