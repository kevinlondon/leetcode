import sys

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        
        longest = left = nums[0]
        for x in range(1, len(nums)):
            num = nums[x]
            if left < 0:
                left = num
            else:
                left += num
                
            if left > longest:
                longest = left
        
                    
        return longest
        