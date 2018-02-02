class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0
        
        prod = None
        
        if n == 2:
            return 1
        elif n == 3:
            return 2
        
        while n:
            if n % 3 == 0 or n >= 5:
                val = 3
            elif n % 2 == 0:
                val = 2
            else:
                val = 1
            
            if not prod:
                prod = val
            else:
                prod *= val
            
            n -= val
        
        return prod