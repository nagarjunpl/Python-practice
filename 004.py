# find the total number of characters in a string without spaces


inp_string = input("Enter a string : ")

a = inp_string.replace(" ", "")   # Remove spaces from the string

count=0   # Initialize character count

for i in a:
    count += 1   # Count each character

print("Total number of characters : ", count)