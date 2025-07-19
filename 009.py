# Write a Python program to sort a list of user-input numbers using the bubble sort algorithm.

# Take input from the user for how many numbers they want to enter
n = int(input("Enter how many numbers: "))

# Initialize an empty list to store the numbers
list2 = []

# Loop to take 'n' inputs from the user and append to the list
for i in range(n):
    list1 = int(input())  # Take one number as input
    list2.append(list1)   # Add the number to the list

# Print the original unsorted list
print("Original list:", list2)

# Bubble Sort Algorithm to sort the list in ascending order
for i in range(n):
    for j in range(n - 1 - i):  # Reduce the range after each pass
        if list2[j] > list2[j + 1]:  # Swap if the current item is greater than the next
            temp = list2[j]
            list2[j] = list2[j + 1]
            list2[j + 1] = temp

# Print the sorted list
print("Sorted list:", list2)
