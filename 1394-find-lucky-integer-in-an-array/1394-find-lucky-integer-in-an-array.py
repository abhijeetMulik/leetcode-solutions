class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = Counter(arr)
        ans = -1
        for k, v in dic.items():
            if k == v:
                ans = max(ans, k)
        return ans
        