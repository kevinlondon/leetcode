from typing import List
import pytest


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        lo, hi = 0, len(height) - 1

        while lo < hi:
            left, right = height[lo], height[hi]
            max_area = max(max_area, min(left, right) * (hi - lo))

            if left <= right:
                lo += 1

            if left >= right:
                hi -= 1

        return max_area


@pytest.mark.parametrize("heights,expected", [
    ([1,8,6,2,5,4,8,3,7], 49),
    ([1,1], 1),
    ([4,3,2,1,4], 16),
    ([1,2,1], 2)
])
def test_max_area(heights, expected):
    assert Solution().maxArea(heights) == expected

