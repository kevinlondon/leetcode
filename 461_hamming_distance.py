from operator import xor

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = self.toBinary(x)
        y = self.toBinary(y)
        
        diff = 0
        for idx in range(len(x)):
            if x[idx] != y[idx]:
                diff += 1
                
        return diff
    
    def toBinary(self, num, bits=32):
        num = bin(num)[2:]
        return num.zfill(bits)