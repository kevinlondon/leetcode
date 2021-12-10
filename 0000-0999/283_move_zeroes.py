class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        
        insert_idx = 0
        for num in nums:
            if num != 0:
                nums[insert_idx] = num
                insert_idx += 1
                
        for x in range(insert_idx, len(nums)):
            nums[x] = 0