import pytest


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        mask = 0xfff
        while (b & mask) > 0:
            carry = a & b
            a = a ^ b
            b = carry << 1

        return (a & mask) if b > 0 else a


@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (2, 3, 5),
    (-1, 1, 0)
])
def test_solution(a, b, expected):
    assert Solution().getSum(a, b) == expected
