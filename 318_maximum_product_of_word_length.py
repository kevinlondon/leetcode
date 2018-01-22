class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        
        length = len(words)
        
        values = [0 for x in range(length)]
        
        for i in range(length):
            word = words[i]
            for j in range(len(word)):
                values[i] |= 1 << (ord(word[j]) - ord('a'))
                
        max_product = 0
        for i in range(length):
            for j in range(i+1, length):
                if ((values[i] & values[j] == 0) and 
                    (len(words[i]) * len(words[j]) > max_product)):
                    max_product = len(words[i]) * len(words[j])
        
        return max_product
                    