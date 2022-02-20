class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        needed = 0
        stack = []
        
        for c in s:
            if c == '(':
                stack.append('(')
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    needed += 1
                    
        needed += len(stack)
        return needed
            
    