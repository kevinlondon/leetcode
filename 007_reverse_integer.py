class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)
        is_negative = x_str.startswith('-')
        x_str = x_str.replace('-', '')
        rev_x = int('{}{}'.format('-' if is_negative else '', x_str[::-1]))
        return rev_x if -2**31 < rev_x < 2**31 else 0
            
        