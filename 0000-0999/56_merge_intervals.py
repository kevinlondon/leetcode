class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        last_interval = None

        result = []
        for interval in intervals:
            if not last_interval or interval[0] > last_interval[1]:
                result.append(interval)
                last_interval = interval
            elif last_interval and interval[0] <= last_interval[1] and interval[1] > last_interval[1]:
                last_interval[1] = interval[1]
                result[-1][1] = interval[1]


        return result
