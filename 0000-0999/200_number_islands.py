from queue import Queue

class Solution:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        height, width = len(grid), len(grid[0])

        def bfs(i, j):
            to_visit = Queue()
            to_visit.put((i, j))

            while not to_visit.empty():
                x, y = to_visit.get()
                if not (0 <= x < width and 0 <= y < height) or grid[y][x] == '0':
                    continue

                grid[y][x] = '0'
                for delta_x, delta_y in self.directions:
                    to_visit.put((x + delta_x, y + delta_y))

        islands = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '1':
                    islands += 1
                    bfs(x, y)

        return islands
