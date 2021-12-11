import pytest

MODULO = (10 ** 9 + 7)


class Solution:

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        # One idea is to have a pair of pointers and check if the value times itself is less than the value times the next in the list.
        # So we have to check the left and right sides of the pair right?

        if a > b:
            a, b = b, a  # just easier to reason about these in order.

        if b % a == 0:
            return (n * a) % MODULO

        answers = []
        next_a, next_b = a, b

        for _ in range(n):
            if next_a < next_b:
                answers.append(next_a)
                next_a += a
            elif next_a > next_b:
                answers.append(next_b)
                next_b += b
            else:
                answers.append(next_a)
                next_a += a
                next_b += b

        return answers[n-1] % MODULO


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
