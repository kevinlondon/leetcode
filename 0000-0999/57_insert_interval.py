class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        i = 0
        inserted = False

        while i < len(intervals):
            interval = intervals[i]
            if newInterval[1] < interval[0] and not inserted:
                intervals.insert(i, newInterval)
                return intervals
            elif interval[0] <= newInterval[0] <= interval[1] or (interval[0] <= newInterval[1] <= interval[1] and not inserted):
                lower = min(interval[0], newInterval[0])
                upper = max(interval[1], newInterval[1])
                newInterval = [lower, upper]
                intervals[i] = newInterval
                inserted = True
                i += 1
            elif ((newInterval[1] >= interval[0] and inserted) or
            (newInterval[0] < interval[0] and newInterval[1] > interval[1])):
                newInterval[1] = max(newInterval[1], interval[1])
                del intervals[i]
            else:
                i += 1

        if not inserted:
            intervals.append(newInterval)
        return intervals
