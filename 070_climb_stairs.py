import pytest


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        x, y = 1, 2

        for _ in range(3, n+1):
            x, y = y, x + y

        return y


@pytest.mark.parametrize("n, expected", [
    (2, 2),
    (3, 3),
    (4, 5)
])
def test_sol(n, expected):
    assert Solution().climbStairs(n) == expected
