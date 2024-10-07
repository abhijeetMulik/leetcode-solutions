class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        ans = 0
        s = list(s)
        while s:
            idx = s.index(s[-1])
            if idx == len(s) -1 :
                ans += idx // 2
            else:
                ans += idx
                s.pop(idx)
            
            s.pop()

        return ans