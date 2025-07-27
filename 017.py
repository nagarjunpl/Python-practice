# Write a Python program that takes a string input and swaps the case of each letter 

# Function to swap the case of each character in the string
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    # Take input from the user
    s = input()
    # Call the function and store the result
    result = swap_case(s)
    # Print the result with swapped cases
    print(result)
