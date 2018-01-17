class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if not x:
            return True
        
        x = str(x)
        is_even = len(x) % 2 == 0
        midpoint = int(len(x) / 2)
        l_bound = midpoint if is_even else midpoint + 1
        r_bound = midpoint
        return x[:l_bound] == x[r_bound:][::-1]
        