class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def closedIsland(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])

        islands = 0

        def floodFill(x, y):
            if 0 <= x < width and 0 <= y < height and grid[y][x] == 0:
                grid[y][x] = 1
                for delta_x, delta_y in self.directions:
                    floodFill(x + delta_x, y + delta_y)

        for y in range(height):
            floodFill(0, y)
            floodFill(width-1, y)

        for x in range(width):
            floodFill(x, 0)
            floodFill(x, height-1)

        for y in range(1, height-1):
            for x in range(1, width-1):
                if grid[y][x] == 0:
                    islands += 1
                    floodFill(x, y)

        return islands
