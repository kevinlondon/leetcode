class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        columns, rows = set(), set()
        n_col, n_row = len(matrix), len(matrix[0])

        for row in range(n_col):
            for column in range(n_row):
                if matrix[row][column] == 0:
                    columns.add(column)
                    rows.add(row)


        for row in rows:
            for col in range(n_row):
                matrix[row][col] = 0

        for row in range(n_col):
            for col in columns:
                matrix[row][col] = 0


        return matrix
