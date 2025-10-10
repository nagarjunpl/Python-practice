# Check if the Number is Armstrong or not

class Solution:
    def isArmstrong(self, n):
        num_str = str(n)
        length = len(num_str)
        total = 0

        for digit in num_str:
            total += int(digit) ** length

        return total == n


a = Solution()
print(a.isArmstrong(153))  # True
print(a.isArmstrong(123))  # False
