class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        low = prices[0]
        for i in range(len(prices)):
            if i != len(prices)-1 and prices[i] < prices[i+1]:
                result += prices[i+1] - prices[i]
            # if prices[i] < low:
            #     low = prices[i]
            # if i>0 or prices[i] > prices[i-1]:
            #     result += prices[i] - low
        return result
        