class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        while n > 3:
            n /= 3
        if n != 3:
            return False
        return True