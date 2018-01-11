OPEN = {
    '(': ')',
    '{': '}',
    '[': ']',
}

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        levels = []
        for character in s:
            if character in OPEN:
                levels.append(character)
            else:
                if not levels:
                    return False
                
                opening_char = levels.pop()
                closing_char = OPEN[opening_char]
                if closing_char != character:
                    return False
        
        return not levels        