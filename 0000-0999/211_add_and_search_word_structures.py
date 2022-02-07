class WordDictionary:

    def __init__(self):
        self.trie = {}


    def addWord(self, word: str) -> None:
        trie = self.trie
        for letter in word:
            if letter not in trie:
                trie[letter] = {}

            trie = trie[letter]

        trie['#'] = True

    def search(self, word: str, trie=None) -> bool:
        if not trie:
            trie = self.trie

        if not word:
            return '#' in trie

        for i, letter in enumerate(word):
            if letter == '.':
                for letter in trie:
                    if letter == '#':
                        continue

                    if self.search(word[i+1:], trie[letter]):
                        return True
                return False
            elif letter not in trie:
                return False
            else:
                trie = trie[letter]

        return '#' in trie


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
