class Solution:
    def countSubstrings(self, s: str) -> int:
        substrs = 0

        for i in range(len(s)):
            substrs += self.expand_around_center(s, i, i)
            substrs += self.expand_around_center(s, i, i+1)

        return substrs

    def expand_around_center(self, s, i, j):
        found = 0

        while 0 <= i and j < len(s) and s[i] == s[j]:
            found += 1
            i -= 1
            j += 1

        return found
