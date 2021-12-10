class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [0]
        
        while len(squares) <= n:
            m = len(squares)
            cntSquares = 500000000
            
            i = 1
            while i**2 <= m:
                cntSquares = min(cntSquares, squares[m - i**2] + 1)
                i += 1
                
            squares.append(cntSquares)
            
        return squares[n]