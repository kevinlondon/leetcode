class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            nums[val] = -abs(nums[val])
            
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]