class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        if len(s) == 0:
            return len(t)
        
        ans, right, left = len(t), 0, 0
        while right < len(s) and left < len(t):
            if s[right] == t[left]:
                ans -= 1
                left += 1
            right += 1

        return ans
