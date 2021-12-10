from collections import defaultdict
from Queue import PriorityQueue


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] += 1
            
        queue = PriorityQueue()
        for val, count in counts.items():
            queue.put((-count, val))
            
        return [queue.get()[1] for x in range(k)]