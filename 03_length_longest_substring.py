class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        mapping = {}
        
        index2 = 0
        for index in xrange(len(s)):
            character = s[index]
            if character in mapping:
                index2 = max(index2, mapping[character] + 1)
                
            mapping[character] = index
            longest = max(longest, index - index2 + 1)
            
        return longest