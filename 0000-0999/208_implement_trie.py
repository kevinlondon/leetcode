class Trie:

    def __init__(self):
        self.trie = defaultdict(dict)

    def insert(self, word: str) -> None:
        if not word:
            return
        trie = self.trie
        for letter in word:
            if letter not in trie:
                trie[letter] = defaultdict(dict)

            trie = trie[letter]

        trie['#'] = True

    def search(self, word: str) -> bool:
        trie = self.trie
        for letter in word:
            if letter not in trie:
                return
            trie = trie[letter]

        return '#' in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for letter in prefix:
            if letter not in trie:
                return
            trie = trie[letter]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
