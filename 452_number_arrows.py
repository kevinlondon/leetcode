from collections import defaultdict

class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x: x[1])
        arrows, end = 0, -float('inf')
        
        for interval in points:
            if interval[0] > end:
                arrows += 1
                end = interval[1]
                
        return arrows