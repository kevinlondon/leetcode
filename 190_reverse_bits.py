import pytest


class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        count = 0
        for x in range(32):
            reverse = (reverse << 1) + (n & 1)
            n >>= 1

        return reverse


@pytest.mark.parametrize("n,expected", [
    (0b00000010100101000001111010011100, 964176192),
    (4294967293, 3221225471),
])
def test_solution(n, expected):
    assert Solution().reverseBits(n) == expected

