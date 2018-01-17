class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = sorted(list(set(nums)))
        length = len(unique_nums)
        print(unique_nums)
        
        for index in range(len(nums)):
            if index < length:
                nums[index] = unique_nums[index]
            else:
                nums[index] = None
                
        return length
        