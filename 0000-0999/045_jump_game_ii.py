class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Idea:
        * Include a minimum number of jumps at each square, then evaluate the minimum
        seen so far
        Do we still start from the end?
        I think so!
        """

        min_jumps = [float('inf')] * len(nums)
        min_jumps[0] = 0

        for i, num in enumerate(nums):
            for j in range(1, num+1):
                if i+j >= len(nums):
                    continue

                min_jumps[i+j] = min(min_jumps[i] + 1, min_jumps[i+j])

        return min_jumps[-1]
