class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def numEnclaves(self, grid: List[List[int]]) -> int:
        """
        Idea:
        Going from the edges of the graph, do DFS until hitting edges
        When finishing going from the edges, any remaining land
        spaces are going to be left, so we can sum the 1s.
        """
        if not grid:
            return 0

        width, height = len(grid[0]), len(grid)

        def dfs(x, y):
            if not (0 <= x < width and 0 <= y < height):
                return

            if not grid[y][x] == 1:
                return

            grid[y][x] = 0
            for delta_x, delta_y in self.directions:
                dfs(x+delta_x, y+delta_y)

        for y in range(height):
            dfs(0, y)
            dfs(width-1, y)

        for x in range(width):
            dfs(x, 0)
            dfs(x, height-1)

        found = 0
        for y in range(height):
            for x in range(width):
                if grid[y][x] == 1:
                    found += 1

        return found
