class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""

        def expand(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1

            return s[start+1:end]

        for i in range(len(s)):
            even = expand(i, i)
            odd = expand(i, i+1)

            if max(len(even), len(odd)) > len(palindrome):
                palindrome = even if len(even) > len(odd) else odd

        return palindrome
