import pytest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums)
        for index, num in enumerate(nums):
            total += index - num

        return total


@pytest.mark.parametrize("nums, expected", [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9,6,4,2,3,5,7,0,1], 8),
    ([0], 1)
])
def test_solution(nums, expected):
    assert Solution().missingNumber(nums) == expected
