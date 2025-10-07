class Solution():
    def pattern(self, n):
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()
            
a = Solution()
a.pattern(5)

'''
OUTPUT
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''
