class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = float('inf')
        hmap = {}
        for i, c in enumerate(cards):
            if c in hmap:
                ans = min(ans, i - hmap[c] + 1)
            hmap[c] = i
        if ans < float('inf'):
            return ans
        else:
            return -1
        