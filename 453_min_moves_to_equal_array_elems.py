class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = min(nums)
        moves = sum([val-min_val for val in nums])
        return moves