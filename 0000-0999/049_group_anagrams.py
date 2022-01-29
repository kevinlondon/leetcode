class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list)

        for word in strs:
            ana[str(sorted(word))].append(word)

        return ana.values()
