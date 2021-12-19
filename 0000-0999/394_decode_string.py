class Solution:
    def decodeString(self, s: str) -> str:
        multiplier = "0"
        substring = ""
        bracket_depth = 0
        for index, character in enumerate(s):
            if character.isdigit():
                if bracket_depth == 0:
                    multiplier += character
                else:
                    multiplier = "0"
            elif character == '[':
                substring += int(multiplier) * self.decodeString(s[index+1:])
                bracket_depth += 1
            elif character == ']':
                multiplier = "0"
                bracket_depth -= 1
                if bracket_depth < 0:
                    return substring
            else:
                if bracket_depth == 0:
                    substring += character

        return substring
