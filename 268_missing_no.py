import pytest
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        to_find = set(range(len(nums) + 1))
        for num in nums:
            to_find.remove(num)

        return next(iter(to_find))


@pytest.mark.parametrize("nums, expected", [
    ([3, 0, 1], 2),
    ([0, 1], 2),
    ([9,6,4,2,3,5,7,0,1], 8),
    ([0], 1)
])
def test_solution(nums, expected):
    assert Solution().missingNumber(nums) == expected
