class Solution:
        
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome = ""
        
        for index in range(len(s)):
            a = self.expandAroundCenter(s, index, index)
            b = self.expandAroundCenter(s, index, index+1)
            
            if max(len(a), len(b)) > (len(palindrome)):
                palindrome = a if len(a) > len(b) else b
            
        return palindrome     
        
    def expandAroundCenter(self, s, left, right):
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        
        return s[left+1:right]