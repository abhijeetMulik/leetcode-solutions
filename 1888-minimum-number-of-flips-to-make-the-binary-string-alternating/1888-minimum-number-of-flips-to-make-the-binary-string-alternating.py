class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        v1, v2 = '', ''
        for i in range(len(s)):
            v1 += '0' if i % 2 == 0 else '1'
            v2 += '1' if i % 2 == 0 else '0'

        ans = float('inf')
        diff1 = 0
        diff2 = 0
        left = 0
        for right in range(len(s)):
            if s[right] != v1[right]:
                diff1 += 1
            if s[right] != v2[right]:
                diff2 += 1
            
            if (right - left + 1) > n:
                if s[left] != v1[left]:
                    diff1 -= 1
                if s[left] != v2[left]:
                    diff2 -= 1
                left += 1
            
            if (right - left + 1) == n:
                ans = min(ans, diff1, diff2)
        
        return ans


