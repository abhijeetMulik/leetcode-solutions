class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(), s.sort()
        i, j, ans = 0, 0, 0
        n, m = len(g), len(s)

        while i < n and j < m:
            if s[j] >= g[i]:
                i += 1
                ans += 1
            j += 1
        
        return ans