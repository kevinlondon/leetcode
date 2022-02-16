import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []

        for point in points:
            distance = (point[0] ** 2 + point[1] ** 2)
            # We want to sort so that the smallest item pops last from the last
            # We want to remove the further item if it's too large.
            if len(closest_points) == k:
                heapq.heappushpop(closest_points, (-distance, point))
            else:
                heapq.heappush(closest_points, (-distance, point))

        return [point for priority, point in closest_points]

