from queue import Queue

class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_seen = 0

        def dfs(x, y):
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and grid[y][x]:
                grid[y][x] = 0
                areas = 1
                for delta_x, delta_y in self.directions:
                    areas += dfs(x+delta_x, y+delta_y)
                return areas
            return 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    max_seen = max(max_seen, dfs(x, y))

        return max_seen
