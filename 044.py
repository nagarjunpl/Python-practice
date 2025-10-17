# Print 1 to N using Recursion

class Solution:
    def printNumbers(self, n):
        if n == 0 :
            return

        self.printNumbers(n - 1)
        print(n)
        
a = Solution()
a.printNumbers(6)
