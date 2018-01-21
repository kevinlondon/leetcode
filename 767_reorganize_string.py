class Solution:
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        forward = self.reorganize(list(S))
        backward = self.reorganize(forward[::-1])
        
        chars = "".join(backward[::-1])
        for i in range(len(chars) - 1):
            if chars[i] == chars[i+1]:
                return ""
        
        return chars
        
    def reorganize(self, chars):
        for i in range(len(chars) - 1):
            char = chars[i]
            j = i + 1
            
            if chars[j] == char:
                swap = j + 1
                while swap < len(chars) and chars[swap] == char:
                    swap += 1
                
                if swap == len(chars):
                    return chars
                else:
                    chars[swap], chars[j] = chars[j], chars[swap]
                    
        return chars
        