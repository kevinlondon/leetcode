class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for i in range(len(nums)):
            comps = []
            if i < 2:
                comps.append(nums[i])

            if i >= 1:
                comps.append(dp[i-1])

            if i >= 2:
                comps.append(dp[i-2] + nums[i])

            if i >= 3:
                comps.append(dp[i-3] + nums[i])

            dp[i] = max(comps)

        return dp[-1]

