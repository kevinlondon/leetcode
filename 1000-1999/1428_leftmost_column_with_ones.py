# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        height, width = binaryMatrix.dimensions()
        min_seen = float('inf')

        eligible_rows = set([i for i in range(height)])
        left = 0
        right = width-1
        while left <= right:
            midpoint = left + ((right-left) // 2)

            found_one = False
            still_good_rows = set()
            for row in eligible_rows:
                if binaryMatrix.get(row, midpoint) == 1:
                    found_one = True
                    still_good_rows.add(row)
                    min_seen = min(min_seen, midpoint)

            if not found_one:
                left = midpoint + 1
            else:
                eligible_rows = still_good_rows
                right = midpoint - 1

        if min_seen != float('inf'):
            return min_seen
        else:
            return -1
