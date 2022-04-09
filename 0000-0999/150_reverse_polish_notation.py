def divide(x, y):
    val = abs(y) // abs(x)
    if (y < 0 and x > 0) or (x < 0 and y > 0):
        val = -val
    return val


OPERATIONS = {
    '+': lambda x,y: y+x,
    '-': lambda x,y: y-x,
    '*': lambda x,y: y*x,
    '/': divide,
}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            signless = c.lstrip("-")
            if signless.isdigit():
                stack.append(int(c))
            else:
                stack.append(OPERATIONS[c](stack.pop(), stack.pop()))

        return stack[-1]
