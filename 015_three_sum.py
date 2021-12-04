from typing import List, Dict, Set, Tuple
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        matches = []
        nums.sort()

        for idx, value in enumerate(nums[:-2]):
            if idx > 0 and value == nums[idx-1]:
                continue

            if value > 0: break

            lo, hi = idx + 1, len(nums) - 1

            while lo < hi:
                total = value + nums[lo] + nums[hi]
                if total == 0:
                    matches.append([value, nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi-1]:
                        hi -= 1

                    lo += 1
                    hi -= 1
                elif total < 0:
                    lo += 1
                else:
                    hi -= 1

        return matches


sol = Solution()

def test_base_case():
    nums = [-1,0,1,2,-1,-4]
    assert sol.threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]

def test_empty_case():
    assert sol.threeSum([]) == []

def test_single_item():
    assert sol.threeSum([0]) == []

def test_all_same_item():
    assert sol.threeSum([0] * 1000) == [[0, 0, 0]]
