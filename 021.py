# Write a program to remove user-given numbers from a list of digits 0–9 and print the remaining numbers.


# Ask the user how many numbers they want to input
n = int(input("Enter how many numbers: "))

# Initialize an empty list to store user inputs
list2 = []

# Collect 'n' numbers from the user
for i in range(1, n + 1):
    num = int(input(f"Enter number {i}: "))
    list2.append(num)  # Add each number to the list

# Store the given numbers in a variable
given_nums = list2

# Initialize a list of digits from 0 to 9
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Loop through the user-provided numbers
for j in given_nums:
    # If the number exists in nums list, remove it
    if j in nums:
        nums.remove(j)
        print(f"Removed: {j}")  # Print which number was removed

# Print the remaining numbers in the list after removal
print("Remaining numbers:", nums)

