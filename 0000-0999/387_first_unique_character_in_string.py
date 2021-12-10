from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = Counter(s)
        for idx, char in enumerate(s):
            if counts[char] == 1:
                return idx
        
        return -1