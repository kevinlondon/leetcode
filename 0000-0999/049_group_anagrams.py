class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(string)
            else:
                anagrams[sorted_str] = [string, ]
            
        anagram_lists = [anagram_list for anagram, anagram_list in anagrams.items()]
        return anagram_lists