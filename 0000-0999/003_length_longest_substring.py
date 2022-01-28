class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        in_string = set()
        longest = 0

        head = 0

        for i, letter in enumerate(s):
            if letter in in_string:
                longest = max(longest, len(in_string))
                remove = s[head]
                while remove != letter and head < i:
                    in_string.remove(remove)
                    head += 1
                    remove = s[head]
                head += 1
                in_string.remove(remove)

            in_string.add(letter)

        longest = max(longest, len(in_string))
        return longest
