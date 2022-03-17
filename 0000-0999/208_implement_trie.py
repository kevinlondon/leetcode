class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for letter in word:
            node = node.children[letter]

        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root

        for letter in word:
            node = node.children.get(letter)
            if not node:
                return False

        return node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for letter in prefix:
            node = node.children.get(letter)
            if not node:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
