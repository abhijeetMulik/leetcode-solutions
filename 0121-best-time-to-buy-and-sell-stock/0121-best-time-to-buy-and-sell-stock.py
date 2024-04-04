class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result= 0
        lowest= prices[0]
        for i in prices:
            if i < lowest:
                lowest = i
            result = max(result, i-lowest)
        return result


            

        