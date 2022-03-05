class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ocean_views = [len(heights) - 1]
        for i in range(len(heights)-2, -1, -1):
            if heights[i] > heights[ocean_views[-1]]:
                ocean_views.append(i)

        return reversed(ocean_views)
