class Solution:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1),
                  (1, 1), (-1, -1), (1, -1), (-1, 1)]
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        level, next_level = [(0, 0)], []
        shortest_path = 1

        if not grid or not grid[0]:
            return -1

        while level:
            x, y = level.pop()

            is_in_bounds = 0 <= x < len(grid[0]) and 0 <= y < len(grid)
            if is_in_bounds and grid[y][x] == 0:
                if x == len(grid[0])-1 and y == len(grid)-1:
                    return shortest_path

                grid[y][x] = '#'
                for delta_x, delta_y in self.directions:
                    next_level.append((x + delta_x, y + delta_y))

            if not level and next_level:
                level = next_level
                next_level = []
                shortest_path += 1

        return -1
