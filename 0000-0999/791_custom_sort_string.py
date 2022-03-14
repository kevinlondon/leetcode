class Solution:
    def customSortString(self, order: str, s: str) -> str:
        char_to_val = {}

        for index, letter in enumerate(order):
            if letter not in char_to_val:
                char_to_val[letter] = index

        return ''.join(sorted(s, key=lambda letter: char_to_val.get(letter, 0)))
