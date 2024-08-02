class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        ans = 0
        for i in s:
            for j in g:
                if j <= i:
                    ans += 1
                    g.remove(j)
                    break
        return ans
        