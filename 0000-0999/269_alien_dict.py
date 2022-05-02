class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words)-1):
            word, word2 = words[i], words[i+1]
            min_length = min(len(word), len(word2))

            if len(word) > len(word2) and word[:min_length] == word2[:min_length]:
                return ""

            for j in range(min_length):
                if word[j] != word2[j]:
                    adj[word[j]].add(word2[j])
                    break

        visited = {}
        ans = []

        def dfs(letter):
            state = visited.get(letter, None)
            if state:
                raise RuntimeError()
            elif state is False:
                return

            visited[letter] = True
            for c in adj[letter]:
                dfs(c)

            ans.append(letter)
            visited[letter] = False

        for c in adj:
            try:
                dfs(c)
            except RuntimeError:
                return ""

        return ''.join(ans[::-1])
