class Solution:
    def isAnswerable(self, index, length):
        isEven = length % 2 == 0
        print(index, length, isEven)
        if (not isEven and (length - 1) / 2 == index) or (isEven and (length - 2) / 2 == index):
            return True
        else:
            return False
        
    def getAnswer(self, x, y, isEven):
        if isEven:
            return (x + y) / 2
        elif x < y:
            return x
        else:
            return y
        
    def getNext(self, index, nums):
        if index < len(nums):
            return nums[index]
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2);
        n1Idx = 0;
        n2Idx = 0;
        isEven = length % 2 == 0;
        
        if length == 0:
            return 0
        
        for count in range(length):
            x = self.getNext(n1Idx, nums1)
            x2 = self.getNext(n1Idx+1, nums1)
            y = self.getNext(n2Idx, nums2)
            y2 = self.getNext(n2Idx+1, nums2)
            
            if self.isAnswerable(count, length):
                if length == 1:
                    return x if x else y
                elif x and y:
                    if x < y:
                        if x2 and x2 < y:
                            return self.getAnswer(x, x2, isEven)
                        else:
                            return self.getAnswer(x, y, isEven)
                    else:
                        if y2 and y2 < x:
                            return self.getAnswer(y, y2, isEven)
                        else:
                            return self.getAnswer(x, y, isEven)
                elif x:
                    return self.getAnswer(x, x2, isEven)
                else:
                    return self.getAnswer(y, y2, isEven)

            if n1Idx + 1 > len(nums1):
                n2Idx += 1
            elif n2Idx + 1 > len(nums2):
                n1Idx += 1
            elif x > y:
                n2Idx += 1
            elif x == y:
                if n1Idx + 1 >= len(nums1):
                    n2Idx += 1
                elif n2Idx + 1 >= len(nums2):
                    n1Idx += 1
                elif x2 > y2:
                    n2Idx += 1
                else:
                    n1Idx += 1
            else:
                n1Idx += 1