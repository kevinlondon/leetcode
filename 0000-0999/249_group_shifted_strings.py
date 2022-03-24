class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        string_groups = defaultdict(list)

        for word in strings:
            distances = []
            for i in range(1, len(word)):
                distances.append((26 + ord(word[i]) - ord(word[i-1])) % 26)

            string_groups[tuple(distances)].append(word)


        return string_groups.values()
