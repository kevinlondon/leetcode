class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n > 0:
            if n == 1:
                return True
            elif n & 1:
                return False
            else:
                n >>= 1

        return False
