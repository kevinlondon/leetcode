class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # key is nums[i] - nums[0] - i

        diffs = [nums[i] - nums[0] - i for i in range(len(nums))]
        insert = bisect.bisect_left(diffs, k)

        if insert == len(nums):
            return k - diffs[-1] + nums[-1]
        else:
            return nums[insert-1] - diffs[insert-1] + k
