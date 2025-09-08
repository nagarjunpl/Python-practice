import math

class Solution:
    def mySqrt(self, x: int) -> int:
        sqrt1 = math.sqrt(x)
        return int(sqrt1)  # truncate the decimal part
