import pytest
from typing import List
from collections import OrderedDict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        counts = OrderedDict([])
        min_count = -1

        if amount == 0: return 0
        loops = 0

        new_counts = {coin: 1 for coin in coins}
        while new_counts:
            counts.update(new_counts)
            if amount in counts:
                return counts[amount]

            new_counts = {}
            for coin, count in counts.items():
                if coin == amount:
                    min_count == amount

                for coin2, count2 in counts.items():
                    combo = coin + coin2
                    tcount = count + count2

                    if combo > amount:
                        break
                    elif combo not in counts and (combo not in new_counts or new_counts[combo] > tcount):
                        new_counts[combo] = tcount

        return min_count




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
