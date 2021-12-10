from enum import Enum


SYMBOLS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}
    
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        last = 0
        
        for symbol in s:
            value = SYMBOLS[symbol]
            total += value
            
            if last < value:
                total -= 2 * last
                
            last = value
        
        return total