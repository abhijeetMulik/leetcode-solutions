class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left = 0
        count = 0
        for right in range(len(s)):
            if left < len(g) and s[right] >= g[left]:
                count += 1
                left += 1
        
        return count




        