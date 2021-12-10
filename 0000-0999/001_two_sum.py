class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        values = {}
        ans = []
        
        for index, x in enumerate(nums):
            if target-x in values:
                return [index, values[target-x]]
                
            values[x] = index