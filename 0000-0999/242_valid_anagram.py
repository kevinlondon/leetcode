class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_c = defaultdict(int)
        t_c = defaultdict(int)

        for c in s:
            s_c[c] += 1

        for c in t:
            t_c[c] += 1

        return s_c == t_c
