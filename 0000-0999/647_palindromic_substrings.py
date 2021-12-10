class Solution:
    
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        pals = 0
        
        for center in range(2*n - 1):
            left = center // 2
            right = left + center % 2
            
            while left >= 0 and right < n and s[left] == s[right]:
                pals += 1
                left -= 1
                right += 1
                
        return pals