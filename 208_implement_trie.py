class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = self.init_tier()
        
    def init_tier(self):
        return [None for x in range(27)]
    
    def chr_to_int(self, char):
        return ord(char) - ord('a')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        tier = self.data
        for char in word:
            idx = self.chr_to_int(char)
            if tier[idx]:
                tier = tier[idx]
            else:
                tier[idx] = self.init_tier()
                tier = tier[idx]
        
        tier[-1] = '*'

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tier = self.data
        for char in word:
            idx = self.chr_to_int(char)
            if not tier[idx]:
                return False
            
            tier = tier[idx]
        return tier[-1] == '*'

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tier = self.data
        for char in prefix:
            idx = self.chr_to_int(char)
            if not tier[idx]:
                return False
            
            tier = tier[idx]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)