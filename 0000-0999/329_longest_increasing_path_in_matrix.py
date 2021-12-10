class Solution:
    
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        longest = 0
        width = len(matrix[0])
        height = len(matrix)
        self.memo = [[None for x in range(width)] for x in range(height)]
        
        for row in range(height):
            for column in range(width):
                longest = max([longest, self.getLength(matrix, row, column)])

        return longest
    
    def isLegal(self, matrix, row, column):
        return (0 <= column < len(matrix[0]) and 0 <= row < len(matrix))
    
    def getLength(self, matrix, row, column):
        if not self.isLegal(matrix, row, column):
            return 0
        
        if self.memo[row][column]:
            return self.memo[row][column]
        
        val = matrix[row][column]
        longest = 0
        options = []
        
        if self.isLegal(matrix, row, column-1) and val < matrix[row][column-1]:
            options.append(self.getLength(matrix, row, column-1))
            
        if self.isLegal(matrix, row, column+1) and val < matrix[row][column+1]:
            options.append(self.getLength(matrix, row, column+1))
        
        if self.isLegal(matrix, row-1, column) and val < matrix[row-1][column]:
            options.append(self.getLength(matrix, row-1, column))
        
        if self.isLegal(matrix, row+1, column) and val < matrix[row+1][column]:
            options.append(self.getLength(matrix, row+1, column))
            
        if options:
            longest = max(options)
        
        longest += 1
        
        self.memo[row][column] = longest
        return longest