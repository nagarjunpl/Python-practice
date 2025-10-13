class Solution:
    def divisors(self, n):
        div = []  # Initialize an empty list to store divisors

        for i in range(1, n + 1):
            if n % i == 0:
                div.append(i)  # Add i to the list of divisors

        return div  
      
a = Solution()

print(a.divisors(8))   # Output: [1, 2, 4, 8]
print(a.divisors(12))  # Output: [1, 2, 3, 4, 6, 12]
print(a.divisors(25))  # Output: [1, 5, 25]
