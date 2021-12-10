class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not n:
            return True
        
        for i, num in enumerate(flowerbed):
            if num:
                continue
                
            j, k = i-1, i+1
            left_open = j < 0 or flowerbed[j] == 0
            right_open = k >= len(flowerbed) or flowerbed[k] == 0
            
            if left_open and right_open:
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
                
        return False