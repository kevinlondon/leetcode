from queue import Queue

class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_seen = 0

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    max_seen = max(max_seen, self.getIslandArea(grid, x, y))

        return max_seen

    def getIslandArea(self, grid: List[List[int]], x: int, y: int) -> int:
        queue = Queue()
        queue.put((x, y))
        area = 0

        while not queue.empty():
            n_x, n_y = queue.get()

            if not (0 <= n_x < len(grid[0]) and 0 <= n_y < len(grid)):
                continue
            elif grid[n_y][n_x] != 1:
                continue

            grid[n_y][n_x] = -1
            area += 1

            for delta_x, delta_y in self.directions:
                i, j = n_x + delta_x, n_y + delta_y
                queue.put((i, j))

        return area
