class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if not arr:
            return 0
        
        chunks = 0
        unique = sorted(set(arr))
        indices = {val: [idx, arr.count(val)] for idx, val in enumerate(unique)}
        needed = [arr.count(x) for x in unique]
        
        max_seen_idx, max_seen_original = -1, -1
        max_comp_idx = 0
        
        for num in arr:
            idx, original = indices[num]
            needed[idx] -= 1
            if idx > max_seen_idx:
                max_seen_idx = idx
                max_seen_original = original
            
            completed = all(needed[idx] == 0 for idx in range(max_comp_idx, max_seen_idx)) and needed[max_seen_idx] != max_seen_original
            
            if completed:
                max_comp_idx = max_seen_idx
                chunks += 1
        
        return chunks
        