from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        full_target = sum(nums)
        if full_target % 2:
            # If the total is not even, it can't be done.
            return False
        target = full_target // 2

        # Pre-initialize to being reachable as false
        dp = [True] + [False] * target
        for x in nums:
            dp = [dp[s] or (s >= x and dp[s-x]) for s in range(target+1)]
            print(x, dp)
            if dp[target]: return True
        return False


if __name__ == '__main__':
    Solution().canPartition([1, 5, 11, 5])
