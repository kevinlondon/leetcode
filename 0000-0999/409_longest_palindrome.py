class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest = 0
        seen = set()
        for c in s:
            if c in seen:
                longest += 2
                seen.remove(c)
            else:
                seen.add(c)

        if seen:
            longest += 1

        return longest
