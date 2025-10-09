# Palindrome Number

class Solution:
    def isPalindrome(self, n):
        n = str(n) 
        rev = n[::-1]
        
        if n == rev :
            print("true")
        else:
            print("false")
            
a = Solution()
a.isPalindrome(121)    # OUTPUT : true
a.isPalindrome(32849)  # OUTPUT : false
