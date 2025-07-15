'''
Take n numbers from the user

Sort them

Display the smallest, largest, and median number

If n is even, also print the difference between the two middle numbers
'''


n = int(input("Enter how many numbers to sort: ")) 

numbers = []   # List to store the numbers

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)   # Append the number to the list

numbers.sort()   # Sort the list of numbers in ascending order

print("Sorted numbers:", numbers)

print("Smallest number:", numbers[0])    # Print the smallest number
print("Largest number:", numbers[-1])    # Print the largest number

# Median calculation

if len(numbers) % 2 == 0:   # Check if the list has an even number of elements
    mid1 = numbers[len(numbers)//2 - 1]    # Get the middle element before the median
    mid2 = numbers[len(numbers)//2]      # Get the middle element after the median
    median = (mid1 + mid2) / 2       # Calculate the median as the average of the two middle elements

    print("Median:", median)

else:
    median = numbers[len(numbers)//2]    # If the list has an odd number of elements, the median is the middle element
    print("Median:", median)
