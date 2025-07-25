# Write a Python program to check if a person is eligible to vote without using if or else.

# Take user's age as input
age = int(input("Enter your age: "))

# Dictionary to map True/False to output messages
output = {
    True: "Eligible to vote",
    False: "Not eligible to vote"
}

# Evaluate age >= 18 and use it as key to print the result
print(output[age >= 18])
