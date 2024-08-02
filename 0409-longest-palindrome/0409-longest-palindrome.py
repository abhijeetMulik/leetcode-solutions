class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        ans = 0
        for i in s:
            if i in seen:
                ans += 2
                seen.discard(i)
            else:
                seen.add(i)
        
        return ans + 1 if len(seen) > 0 else ans
        