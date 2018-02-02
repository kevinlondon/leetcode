class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        self_dividing = []
        
        for i in range(left, right+1):
            chars = str(i)
            is_self_dividing = True
            for c in chars:
                if int(c) == 0 or i % int(c) != 0:
                    is_self_dividing = False
            
            if is_self_dividing:
                self_dividing.append(i)
        
        return self_dividing