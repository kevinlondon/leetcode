from collections import defaultdict


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        two_sum = self.build_two_sum(A, B)
        total_matches = 0
        
        for num_c in C:
            for num_d in D:
                subtotal = num_c + num_d
                complement = 0 - subtotal
                if complement in two_sum:
                    total_matches += two_sum[complement]
        
        return total_matches
    
    def build_two_sum(self, A, B):
        two_sum = defaultdict(int)
        for a in A:
            for b in B:
                two_sum[a+b] += 1
        
        return two_sum