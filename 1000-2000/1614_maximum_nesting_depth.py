class Solution:
    def maxDepth(self, s: str) -> int:
        largest = 0
        stack = []

        for letter in s:
            if letter == '(':
                stack.append(letter)
                largest = max(len(stack), largest)
            elif letter == ')' and stack:
                stack.pop()

        return largest


# Stackless approach
class Solution:
    def maxDepth(self, s: str) -> int:
        largest = 0
        current = 0

        for letter in s:
            if letter == '(':
                current += 1
                largest = max(current, largest)
            elif letter == ')':
                current -= 1

        return largest
