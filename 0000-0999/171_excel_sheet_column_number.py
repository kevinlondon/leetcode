class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return
        
        column = 0
        
        for idx in range(len(s) - 1, -1, -1):
            power = len(s) - idx - 1
            value = self.getValue(s[idx])
            column += value * (26 ** power)
            
        return column
    
    def getValue(self, char):
        return ord(char) - ord('A') + 1