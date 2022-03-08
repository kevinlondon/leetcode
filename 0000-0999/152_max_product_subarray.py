class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_subarray, min_subarray = nums[0], nums[0]
        max_seen = nums[0]

        for num in nums[1:]:
            if num < 0:
                max_subarray, min_subarray = min_subarray, max_subarray

            max_subarray = max(max_subarray * num, num)
            min_subarray = min(min_subarray * num, num)
            max_seen = max(max_subarray, max_seen)

        return max_seen
