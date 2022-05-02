class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = [[] for _ in range(len(words))]
        freq_words = []

        word_counts = defaultdict(int)
        for word in words:
            word_counts[word] += 1

        for word, count in word_counts.items():
            word_count[count-1].append(word)

        for i in range(len(words)-1, -1, -1):
            words = sorted(word_count[i])

            for word in words:
                freq_words.append(word)
                k -= 1
                if k == 0:
                    return freq_words
