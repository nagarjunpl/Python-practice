class Solution():
    def pattern(self, n):
        for i in range(1, n + 1):
            print("*" * n)
        
inp = int(input("Enter how many lines of stars you want : "))
a=Solution()
a.pattern(inp)
