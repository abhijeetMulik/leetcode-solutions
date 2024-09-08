class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = ans = 0
        for right, val in enumerate(s):
            while val in seen:
                seen.discard(s[left])
                left += 1
            seen.add(val)
            ans = max(ans, right - left + 1)
        return ans
        


        