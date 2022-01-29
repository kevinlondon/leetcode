class Solution:
    opposites = {
        '}': '{',
        ']': '[',
        ')': '(',
    }
    def isValid(self, s: str) -> bool:
        openers = []

        for c in s:
            if c not in self.opposites:
                openers.append(c)
            elif not openers or openers[-1] != self.opposites[c]:
                return False
            else:
                openers.pop(-1)

        if openers:
            return False

        return True

