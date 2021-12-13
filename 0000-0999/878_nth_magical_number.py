import pytest
from math import gcd

MODULO = (10 ** 9 + 7)


class Solution:

    def lcm(self, a: int, b: int) -> int:
        return (a * b) // gcd(a, b)

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm_ab = self.lcm(a, b)
        seq = set()

        for x in range(1, lcm_ab // a + 1):
            # 1, (40 // 10) + 1 -> 5
            # 10, 20, 30, 40
            seq.add(x*a)

        for x in range(1, lcm_ab // b + 1):
            # 1, (40 // 8) +1 -> 6
            # 8, 16, 24, 32, 40
            seq.add(x*b)

        ordered = sorted(seq)
        # 8, 10, 16, 20, 24, 30, 32, 40
        full_loops = (n-1) // len(ordered)
        ans = full_loops * lcm_ab + ordered[n % len(ordered)-1]
        # ((10-1) // (8) -> 1 * 40 -> 40 + ordered[10 % 8 - 1] -> ordered[1] -> 10
        # lcm = 40
        return ans % MODULO


@pytest.mark.parametrize("n,a,b,exp", [
    (1, 2, 3, 2),
    (4, 2, 3, 6),
    (5, 2, 4, 10),
    (3, 6, 4, 8),
    (3, 8, 3, 8),
    (10, 10, 8, 50),
])
def test_solution(n, a, b, exp):
    assert Solution().nthMagicalNumber(n, a, b) == exp
