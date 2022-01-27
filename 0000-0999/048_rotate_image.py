class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for loop in range(len(matrix) // 2):
            for i in range(loop, len(matrix) - loop - 1):
                rot = len(matrix) - 1
                a, b, c, d = matrix[loop][i], matrix[i][rot-loop], matrix[rot-loop][rot-i], matrix[rot-i][loop]
                matrix[loop][i], matrix[i][rot-loop], matrix[rot-loop][rot-i], matrix[rot-i][loop] = d, a, b, c
