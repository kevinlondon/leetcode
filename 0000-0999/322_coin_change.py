import pytest
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        min_count = -1
        coin_index = len(coins) - 1

        if amount == 0:
            return 0

        while coin_index >= 0 and amount > 0:
            print(coin_index, amount, min_count)
            coin = coins[coin_index]
            if coin > amount:
                coin_index -= 1
            else:
                amount -= coin
                if min_count < 1:
                    min_count = 1
                else:
                    min_count += 1

        return min_count if coin_index >= 0 else -1


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
