class Solution():
    def pattern(self, n):
        
        for i in range(n):
            print("  " * (n-i-1), end="")
            print("* " * (2*i+1))
        print()   
            
a = Solution()
a.pattern(6)

'''
OUTPUT
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
* * * * * * * * * * * 
'''
