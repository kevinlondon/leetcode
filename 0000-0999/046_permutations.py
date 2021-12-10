
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        elif len(nums) == 1:
            return [nums]
        
        permutations = []
        for i in range(len(nums)):
            sub_perms = self.permute(nums[:i] + nums[i+1:])
            for perm in sub_perms:
                perm.append(nums[i])
                permutations.append(perm)
                
        return permutations