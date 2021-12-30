class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        return max(self.robHouses(nums, 0, len(nums)-1),
                   self.robHouses(nums, 1, len(nums)))

    def robHouses(self, nums: List[int], start: int, stop: int) -> int:
        prev2, prev1 = 0, 0

        for i in range(start, stop):
            prev2, prev1 = prev1, max(prev2 + nums[i], prev1)

        return prev1
