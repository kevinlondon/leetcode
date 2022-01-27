class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        d_idx = 0
        y, x = 0, 0

        spiral = []

        direction = directions[d_idx]


        def in_bounds(x, y):
            return (0 <= y < len(matrix) and 0 <= x < len(matrix[0]))

        while in_bounds(x, y) and visited[y][x] != 1:
            visited[y][x] += 1
            spiral.append(matrix[y][x])
            n_y, n_x = y+direction[0], x+direction[1]
            # Out of bounds check or previously visited check
            if not(in_bounds(n_x, n_y)) or visited[n_y][n_x] == 1:
                d_idx += 1
                direction = directions[d_idx % len(directions)]

            y, x = y + direction[0], x+direction[1]
        return spiral
