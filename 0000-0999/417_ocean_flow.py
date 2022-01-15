class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return [[]]

        m, n = len(heights), len(heights[0])

        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        results = []

        def dfs(i, j, visited):
            visited[i][j] = True

            for (y_delta, x_delta) in directions:
                y, x = i + y_delta, j + x_delta
                if 0 <= y < m and 0 <= x < n and heights[y][x] >= heights[i][j] and not visited[y][x]:
                    dfs(y, x, visited)

        for row in range(m):
            dfs(row, 0, p_visited)
            dfs(row, n-1, a_visited)

        for col in range(n):
            dfs(0, col, p_visited)
            dfs(m-1, col, a_visited)

        for i in range(m):
            for j in range(n):
                if a_visited[i][j] and p_visited[i][j]:
                    results.append([i, j])

        return results
