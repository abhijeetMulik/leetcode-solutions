class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        ans = 0
        curr = 0
        for w in weight:
            curr += w
            if curr > 5000:
                break
            ans += 1
            
        return ans

        