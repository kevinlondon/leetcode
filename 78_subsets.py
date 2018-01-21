class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        
        if len(nums) == 1:
            return [
                [nums[0], ],
                [],
            ]
        else:
            with_num = [[nums[0]] + subset for subset in self.subsets(nums[1:])]
            without_num = self.subsets(nums[1:])
            return with_num + without_num