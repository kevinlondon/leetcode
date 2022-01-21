class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end, count = float('-inf'), 0
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end:
                end = e
            else:
                count += 1

        return count
