from typing import List, Dict, Set, Tuple
from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        matches = set()

        nums = self.trimNums(nums)
        sums = self.twoSum(nums)

        for idx, value in enumerate(nums):
            inverse = -value
            if inverse not in sums:
                continue

            pairs = sums[inverse]
            for pair in pairs:
                if idx in pair:
                    continue

                match = tuple(sorted([nums[idx], nums[pair[0]], nums[pair[1]]]))
                matches.add(match)


        return [list(match) for match in matches]

    def trimNums(self, nums: List[int]) -> List[int]:
        trimmed_nums = []
        seen = defaultdict(int)
        for num in nums:
            if seen.get(num, 0) > 3:
                continue
            trimmed_nums.append(num)
            seen[num] += 1

        return trimmed_nums

    def twoSum(self, nums: List[int]) -> Dict[int, Tuple[List[int], Set[int]]]:
        sums = defaultdict(list)

        for index, value in enumerate(nums[:-1]):
            for index2, value2 in enumerate(nums[index+1:], start=index+1):
                sums[value + value2].append([index, index2])

        return sums


sol = Solution()

def test_base_case():
    nums = [-1,0,1,2,-1,-4]
    assert sol.threeSum(nums) == [[-1, 0, 1], [-1, -1, 2]]

def test_empty_case():
    assert sol.threeSum([]) == []

def test_single_item():
    assert sol.threeSum([0]) == []

def test_all_same_item():
    assert sol.threeSum([0] * 1000) == [[0, 0, 0]]
