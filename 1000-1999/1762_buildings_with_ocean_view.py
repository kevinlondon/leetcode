class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_heights = [0] * (len(heights)+1)
        highest_seen = 0
        ocean_views = []

        for i, height in enumerate(heights[::-1]):
            highest_seen = max(highest_seen, height)
            max_heights[len(heights)-1-i] = highest_seen

        for i, height in enumerate(heights):
            if height > max_heights[i+1]:
                ocean_views.append(i)

        return ocean_views
