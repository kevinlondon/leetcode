class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        # index in word
        i = 0

        move = 0

        for character in abbr:
            if character.isdigit():
                delta = int(character)
                if move:
                    move *= 10
                elif not delta:
                    return False
                move += delta
            else:
                if move:
                    i += move
                    move = 0

                if i < len(word) and character == word[i]:
                    i += 1
                else:
                    return False
        if move:
            i += move
        return i == len(word)
