class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set()
        
        if not matrix:
            return
        
        for y, row in enumerate(matrix):
            if not row:
                return
            
            for x, elem in enumerate(row):
                if elem == 0:
                    rows.add(y)
                    columns.add(x)
                    
        for row in rows:
            matrix[row] = [0 for x in range(len(matrix[row]))]
            
        for column in columns:
            for y in range(len(matrix)):
                matrix[y][column] = 0