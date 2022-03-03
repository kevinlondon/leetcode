class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Given int nums
        Start at the first index (0th index?)
        True if can reach last index.
        """

        jump_needed = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if nums[i] + i >= jump_needed:
                jump_needed = i

        return jump_needed == 0
