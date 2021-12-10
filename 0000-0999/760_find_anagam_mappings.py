from collections import defaultdict


class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        b_map = self.build_map(B)
        if not A or not B:
            return []
        
        a_map_array = []
        for num in A:
            a_map_array.append(b_map[num].pop())
        
        return a_map_array
        
    
    def build_map(self, array):
        array_map = defaultdict(list)
        for idx, num in enumerate(array):
            array_map[num].append(idx)
        
        return array_map