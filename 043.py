class Solution:
    def isPrime(self, n):
        # Prime numbers are greater than 1
        if n <= 1:
            return False

        # Check divisibility from 2 to n-1
        for i in range(2, n):
            if n % i == 0:  # If divisible, not prime
                return False

        # If no divisors found, it's prime
        return True

a = Solution()

print(a.isPrime(5))   # Output: True
print(a.isPrime(8))   # Output: False
print(a.isPrime(13))  # Output: True
print(a.isPrime(1))   # Output: False
