class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        for x in range(1, n+1):
            if x % 15 == 0:
                out.append('FizzBuzz')
            elif x % 5 == 0:
                out.append('Buzz')
            elif x % 3 == 0:
                out.append('Fizz')
            else:
                out.append(str(x))
        
        return out
        