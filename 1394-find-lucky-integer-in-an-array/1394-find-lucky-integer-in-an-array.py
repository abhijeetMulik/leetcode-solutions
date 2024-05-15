class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = 0
        freq = Counter(arr)
        for k, v in freq.items():
            if k == v:
                ans = max(ans, k)
        return ans if ans > 0 else -1