import operator

class Solution(object):
    def productExceptSelf(self, nums):
        zeroes = nums.count(0)
        if not zeroes:
            product = reduce(operator.mul, nums)
            return [product / x for x in nums]
        
        products = [0] * len(nums)
        if zeroes == 1:
            products[nums.index(0)] = reduce(operator.mul, (x for x in nums if x))
        
        return products