import random

class Solution:

    def __init__(self, w: List[int]):
        self.total = 0
        self.selections = []
        for num in w:
            self.total += num
            self.selections.append(self.total)

    def pickIndex(self) -> int:
        to_pick = random.randint(1, self.total)
        return self.binarySearch(to_pick)

    def binarySearch(self, num):
        left, right = 0, len(self.selections)-1
        while left <= right:
            midpoint = left + (right-left)//2
            if ((num <= self.selections[midpoint] and midpoint == 0) or
                (midpoint > 0 and self.selections[midpoint-1] < num <= self.selections[midpoint])):
                return midpoint
            elif num < self.selections[midpoint]:
                right = midpoint-1
            else:
                left = midpoint+1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
