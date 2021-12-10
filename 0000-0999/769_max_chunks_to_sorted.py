class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        
        chunks = 0
        seen = [False for x in range(len(arr))]
        max_seen = -1
        max_comp = -1
        
        for num in arr:
            seen[num] = True
            if num > max_seen:
                max_seen = num
                
            completed = all(seen[max_comp+1:max_seen+1])
            if completed:
                max_comp = max_seen
                chunks += 1
        
        return chunks
        