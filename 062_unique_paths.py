class Solution:
    
    def __init__(self):
        self.memo = []
        
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not self.memo:
            self.memo = [[0 for x in range(n)] for y in range(m)]
            
        if not m or not n:
            return 0
        
        if (m, n) == (1, 1):
            return 1
        
        if self.memo[m-1][n-1]:
            return self.memo[m-1][n-1]
        
        right = self.uniquePaths(m, n-1) if n > 1 else 0
        down = self.uniquePaths(m-1, n) if m > 1 else 0
        self.memo[m-1][n-1] = right + down
        return right + down