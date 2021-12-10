from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points or len(points) < 3:
            return 0
        
        boomerangs = 0
        
        for p in points:
            cmap = defaultdict(int)
            for q in points:
                f = p[0] - q[0]
                s = p[1] - q[1]
                cmap[f**2 + s**2] += 1
            
            for k in cmap:
                boomerangs += cmap[k] * (cmap[k] - 1)
                
        return boomerangs