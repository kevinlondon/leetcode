class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Idea:
        Ladder and stairs.
        """
        jumps, ladder_end, next_furthest = 0, 0, 0

        for i, num in enumerate(nums):
            if i == len(nums)-1:
                break

            next_furthest = max(next_furthest, num + i)

            if i == ladder_end:
                ladder_end = next_furthest
                jumps += 1

        return jumps
