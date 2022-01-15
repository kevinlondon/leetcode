class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return [[]]

        m, n = len(heights), len(heights[0])

        p_visited = set()
        a_visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        results = []

        def dfs(i, j, visited):
            if (i, j) in visited:
                return

            visited.add((i, j))
            for (y_delta, x_delta) in directions:
                y, x = i + y_delta, j + x_delta
                if 0 <= y < m and 0 <= x < n and heights[y][x] >= heights[i][j]:
                    dfs(y, x, visited)

        for row in range(m):
            dfs(row, 0, p_visited)
            dfs(row, n-1, a_visited)

        for col in range(n):
            dfs(0, col, p_visited)
            dfs(m-1, col, a_visited)

        return list(a_visited & p_visited)
