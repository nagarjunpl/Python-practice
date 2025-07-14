# Write a Python program to count the number of vowels in a given name entered by the user.


input_str = input("Enter your name : ")

count = 0

for i in input_str:  # Loop through each character in the input string
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U": # Check if the character is a vowel (either lowercase or uppercase)
        count += 1  # Increment the count if a vowel is found

print(f"Numbers of Ovels in your name is : {count}") # Print the total number of vowels found in the name