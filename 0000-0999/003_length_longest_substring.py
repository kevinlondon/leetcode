class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = longest = 0
        used = {}
        for i, letter in enumerate(s):
            if letter in used and start <= used[letter]:
                start = used[letter] + 1
            else:
                longest = max(longest, i - start + 1)

            used[letter] = i

        return longest
