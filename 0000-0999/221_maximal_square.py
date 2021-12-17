class Solution:
    """
    Runtime: O(mn)
    Space: O(n) where n is columns
    """
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * (cols + 1)

        largest = prev = 0
        for r in range(rows):
            for c in range(cols):
                temp = dp[c+1]

                if matrix[r][c] == '1':
                    dp[c+1] = min(dp[c], dp[c+1], prev) + 1
                    largest = max(largest, dp[c+1])
                else:
                    dp[c+1] = 0

                prev = temp

        return largest ** 2
