class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        bits = []
        for x in range(num+1):
            bits.append(bin(x).count('1'))
        
        return bits