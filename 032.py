class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases
        # If there is only 1 step → only 1 way (just climb 1 step)
        if n == 1:
            return 1
        # If there are 2 steps → two ways: (1+1) or (2)
        if n == 2:
            return 2

        # Initialize for bottom-up DP
        one, two = 1, 2  

        # Start from step 3 up to n
        for i in range(3, n + 1):
            # Current ways = sum of previous two steps
            one, two = two, one + two

        # Finally, 'two' holds the result for n
        return two
