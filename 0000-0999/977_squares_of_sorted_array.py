from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        heap = []
        
        i = 0
        for i, num in enumerate(nums):
            if num > 0:
                break
        
        i, j = i-1, i
        
        while i >= 0 or j < len(nums):
            if i >= 0 and j < len(nums):
                left, right = nums[i], nums[j]
                if abs(left) >= abs(right):
                    heap.append(right**2)
                    j += 1
                else:
                    heap.append(left**2)
                    i -= 1
            elif i >= 0:
                heap.append(nums[i]**2)
                i -= 1
            elif j < len(nums):
                heap.append(nums[j]**2)
                j += 1
        
        return heap