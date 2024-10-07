class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        hmap = {}
        ans = []

        for i, p in enumerate(prices):
            while stack and prices[stack[-1]] >= p:
                hmap[stack.pop()] = p
            stack.append(i)

        while stack:
            hmap[stack.pop()] = 0
        for i, p in enumerate(prices):
            ans.append(p - hmap[i])

        return ans
