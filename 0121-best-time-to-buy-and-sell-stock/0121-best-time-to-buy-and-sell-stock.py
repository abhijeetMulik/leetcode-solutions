class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = 0
        for p in range(1, len(prices)):
            if prices[p] < buy:
                buy = prices[p]
            else:
                sell = max(sell, prices[p] - buy)
        
        return sell

