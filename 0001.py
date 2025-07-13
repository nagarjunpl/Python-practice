'''This program that takes a string input and prints the position of each alphabet letter (a=1 to z=26), 
 ignoring case and non-letter characters'''

import string  # Import the string module

str = input("Enter a string : ") # Take input from the user

a1 = str.lower() # Convert the input string to lowercase

for i in a1:
    if i.isalpha(): # Check if the character is an alphabet letter
        value1 = string.ascii_lowercase.index(i) + 1   # Find the position of the letter in the alphabet
        print(f"{i} = {value1}")
