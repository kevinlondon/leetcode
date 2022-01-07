class Solution:
    visited = set()

    def canJump(self, nums: List[int]) -> bool:
        self.visited = set()
        return self.canJumpFrom(nums, 0)

    def canJumpFrom(self, nums: List[int], start: int) -> bool:
        self.visited.add(start)

        if start >= len(nums) - 1:
            return True

        for x in range(1, nums[start] + 1):
            if start + x not in self.visited and self.canJumpFrom(nums, start+x):
                return True

        return False
