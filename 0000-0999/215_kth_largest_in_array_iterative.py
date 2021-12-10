class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MIN = -50000000
        largest = [MIN for x in range(k)]
        for num in nums:
            if largest[0] == MIN or largest[0] < num:
                largest.append(num)
                largest.sort()
                largest = largest[1:]
        
        return largest[0]