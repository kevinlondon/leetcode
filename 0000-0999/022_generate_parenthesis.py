class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        parens = []
        self.backtrack(parens, "", idx_open=0, idx_close=0, max_n=n)
        return parens
    
    def backtrack(self, parens, string, idx_open, idx_close, max_n):
        if len(string) == max_n * 2:
            parens.append(string)
            return
        
        if idx_open < max_n:
            self.backtrack(parens, string + '(', idx_open+1, idx_close, max_n)
        
        if idx_close < idx_open:
            self.backtrack(parens, string + ')', idx_open, idx_close+1, max_n)
        