class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i, j = cost[0], cost[1]

        for n in range(2, len(cost)):
            i, j = j, min(i + cost[n], j + cost[n])

        return min(i, j)
