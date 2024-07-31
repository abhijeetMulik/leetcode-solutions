class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        limit = 5000
        ans = 0
        for w in weight:
            if limit <= 0 or w > limit:
                break
            limit -= w
            ans += 1
        return ans


        