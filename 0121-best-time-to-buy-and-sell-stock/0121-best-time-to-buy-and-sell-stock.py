class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        profit = prices[0]
        for p in range(len(prices)):
            if prices[p] > profit:
                ans = max(ans, prices[p] - profit)
            else:
                profit = prices[p]
        
        return ans
                