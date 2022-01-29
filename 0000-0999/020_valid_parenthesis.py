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
            elif not openers or openers.pop() != self.opposites[c]:
                return False

        if openers:
            return False

        return True

