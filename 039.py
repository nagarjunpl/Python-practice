# Reverse a number

class Solution:
    def reverseNumber(self, n):
        s = str(n)
        reverse = s[::-1]
        print(int(reverse)) # OUTPUT : 987654321

a = Solution()
a.reverseNumber(123456789)
