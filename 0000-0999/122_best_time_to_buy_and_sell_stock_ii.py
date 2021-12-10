class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        purchase_price = None
        
        for x in range(len(prices) - 1):
            today = prices[x]
            tomorrow = prices[x+1]
            
            if today > tomorrow and purchase_price is not None:
                profit += today - purchase_price
                purchase_price = None
            elif today < tomorrow and purchase_price is None:
                purchase_price = today
        
        if purchase_price is not None and prices[x+1] > purchase_price:
            profit += prices[x+1] - purchase_price
            
        return profit