class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        index = 1
        for i, num in enumerate(nums):
            if i > 0 and num != nums[i-1]:
                nums[index] = num
                index += 1
                
        return index