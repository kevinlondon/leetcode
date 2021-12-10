class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
            
        i = 0
        for color, count in enumerate(counts):
            for x in range(count):
                nums[i] = color
                i += 1
        