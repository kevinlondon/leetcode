class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        longest_seen = 0

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for x in range(1, len(text1) + 1):
            for y in range(1, len(text2)+1):
                if text1[x-1] == text2[y-1]:
                    dp[x][y] = dp[x-1][y-1] + 1
                else:
                    dp[x][y] = max(dp[x-1][y], dp[x][y-1])

                longest_seen = max(longest_seen, dp[x][y])
        return longest_seen


