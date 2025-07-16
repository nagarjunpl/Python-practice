# Check if the number is an Armstrong number or not

a = int(input("Enter a number to check if it's an Armstrong number : "))
print()

total = 0   # This will store the sum of digits raised to the power of the number of digits

for i in str(a):
    print(f"{i}^{len(str(a))} = {int(i) ** len(str(a))}")    # Print each digit raised to the power of the number of digits

    digit = int(i)       # Convert the digit back to integer
    total += digit ** len(str(a))     # Add the digit raised to the power of the number of digits to the total
    
# Check if the calculated total is equal to the original number
if total == a:
    print(f"= {a} is an Armstrong number.\n")
else:
    print(f"= {a} is not an Armstrong number.\n")

