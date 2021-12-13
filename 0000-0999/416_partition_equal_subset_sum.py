from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target, n, memo = sum(nums), len(nums), {0: True}
        if target & 1: return False
        nums.sort(reverse=True)

        def dfs(i, x):
            if x not in memo:
                memo[x] = False
                if x > 0:
                    for j in range(i, n):
                        if dfs(j+1, x-nums[j]):
                            memo[x] = True
                            break
            return memo[x]
        return dfs(0, target >> 1)



if __name__ == '__main__':
    print(Solution().canPartition([6, 3, 3, 2, 2, 2]))
