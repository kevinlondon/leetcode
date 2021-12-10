class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        
        found = set()
        for num in nums:
            if num in found:
                found.remove(num)
            else:
                found.add(num)
        
        return found.pop()