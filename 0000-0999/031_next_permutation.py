class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = self.find_longest_non_increasing_suffix(nums)
        if pivot != -1:
            next_prefix = self.last_index_greater(nums, nums[pivot])
            nums[pivot], nums[next_prefix] = nums[next_prefix], nums[pivot]

        self.reverse_suffix(nums, pivot+1)  # reverse full list if no pivot

    """
    Return the first element of the non-increasing suffix

    For example, in: 0125330, 5 is the first value, so index will be 3 (0 indexed).
    """
    def find_longest_non_increasing_suffix(self, nums):
        last = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < last:
                return i
            else:
                last = nums[i]
        return -1

    def last_index_greater(self, nums, pivot):
        for i in range(len(nums)-1, -1, -1):
            if pivot < nums[i]:
                return i

    """Reverse numbers starting from the end"""
    def reverse_suffix(self, nums, start):
        end = len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
