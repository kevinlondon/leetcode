class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        longest = 0
        
        for index, char in enumerate(strs[0]):
            for string in strs[1:]:
                if (len(string) > index and string[index] == char):
                    pass
                else:
                    return strs[0][:longest]
            longest += 1
        
        return strs[0][:longest]