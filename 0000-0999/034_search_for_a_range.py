class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        num = None
        if not nums:
            return res
        
        midpoint = self.binarySearch(nums, target)
        if midpoint is None:
            return res
        
        i = j = midpoint
        while nums[i] == nums[j] == target:
            if i > 0 and nums[i-1] == target:
                i -= 1
            elif j < len(nums) - 1 and nums[j+1] == target:
                j += 1
            else:
                break
        
        res = [i, j]
            
        return res
        
        
    def binarySearch(self, nums, target):
        
        i = 0
        j = len(nums)
        while i >= 0 and j <= len(nums) and i < j:
            midpoint = (i+j) // 2
            num = nums[midpoint]
            
            if num == target:
                return midpoint
            elif num < target:
                i = midpoint + 1
            else:
                j = midpoint
        
        return None
                
