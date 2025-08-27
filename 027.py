# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers are not palindromes(because of the minus sign)
        if x < 0:
            return False
        
        # Convert the number to a string
        s = str(x)
        
        # Check if the string is equal to its reverse
        return s == s[::-1]
