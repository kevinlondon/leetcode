STONE = '#'
OBSTACLE = '*'
EMPTY = '.'


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        """
        Obstacles:
        Stone = '#'
        Stationary Object = '

        Ideas:
        Maybe we start from the end of the array and build out the bottom rows first.
        We can initialize the array to be the length we expect for all the items.
        Then iterate from end of the array.
        When we find an open cell (e.g. no obstacle, no rock),
        we iterate back up the list until we find an obstacle to swap into that space.
        After that, should fill in empty spaces we've skipped.
        """
        if not box:
            return box

        m, n = len(box), len(box[0])
        rot_box = [['.' for x in range(m)] for y in range(n)]

        # another idea: what if we could blocks between obstacles?

        blocks_until_obstacles = [[] for y in range(m)]

        for y in range(m):
            stones = 0
            for x in range(n):
                if box[y][x] == OBSTACLE:
                    blocks_until_obstacles[y].append(stones)
                    stones = 0
                elif box[y][x] == STONE:
                    stones += 1
            blocks_until_obstacles[y].append(stones)

        for y in range(m-1, -1, -1):
            blocks_for_row = blocks_until_obstacles[y].pop()
            for x in range(n-1, -1, -1):
                if box[y][x] == OBSTACLE:
                    rot_box[x][m-y-1] = OBSTACLE
                    blocks_for_row = blocks_until_obstacles[y].pop()
                    continue
                elif blocks_for_row > 0:
                    rot_box[x][m-y-1] = STONE
                else:
                    rot_box[x][m-y-1] = EMPTY

                blocks_for_row -= 1

        return rot_box
