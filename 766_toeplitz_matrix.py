class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        
        for i in range(len(matrix)):
            if not self.valid_diagonal(matrix, i, 0):
                return False
            
        for j in range(len(matrix[0])):
            if not self.valid_diagonal(matrix, 0, j):
                return False
            
        return True
    
    def valid_diagonal(self, matrix, i, j):
        elem = matrix[i][j]
        
        while i < len(matrix) and j < len(matrix[0]):
            if elem != matrix[i][j]:
                return False
            i += 1
            j += 1
            
        return True