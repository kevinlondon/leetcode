class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1

        if n == 0:
            return a
        elif n == 1:
            return b
        elif n == 2:
            return c

        for i in range(3, n+1):
            a, b, c = b, c, a+b+c

        return c
