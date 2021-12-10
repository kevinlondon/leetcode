from collections import defaultdict


class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = []
        by_height = defaultdict(list)
        
        for person in people:
            by_height[person[0]].append(person[1])
            
        for height in sorted(by_height)[::-1]:
            for in_front in sorted(by_height[height]):
                queue.insert(in_front, [height, in_front])
        
        return queue