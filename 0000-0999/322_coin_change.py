import pytest
from typing import List
from collections import OrderedDict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float('inf') for i in range(amount)]

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        if dp[-1] == float('inf'):
            return -1
        return dp[-1]



@pytest.mark.parametrize("coins, amount, expected", [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1], 1, 1),
    ([1], 2, 2),
    ([186,419,83,408], 6249, 20),
])
def test_solution(coins, amount, expected):
    assert Solution().coinChange(coins, amount) == expected
