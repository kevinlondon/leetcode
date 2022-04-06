class Solution:
    def removeDuplicates(self, s: str) -> str:
        new_s = []

        for letter in s:
            if new_s and new_s[-1] == letter:
                new_s.pop()
            else:
                new_s.append(letter)

        return ''.join(new_s)
