class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMax = float('-inf')
        for i, num in enumerate(nums):
            if i > 0:
                nums[i] = max(nums[i], nums[i] + nums[i-1])
            globalMax = max(nums[i], globalMax)

        return globalMax
