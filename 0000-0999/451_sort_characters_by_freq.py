class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)

        new_str = []
        for letter, count in counts.most_common():
            new_str.append(letter * count)

        return ''.join(new_str)
