class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_order = {letter: index for index, letter in enumerate(order)}

        if len(words) <= 1:
            return True

        prev_nums = []
        for i, word in enumerate(words):
            word_nums = []
            for letter in word:
                word_nums.append(alien_order.get(letter, float('inf')))

            if prev_nums:
                if word_nums < prev_nums:
                    return False

            prev_nums = word_nums

        return True
