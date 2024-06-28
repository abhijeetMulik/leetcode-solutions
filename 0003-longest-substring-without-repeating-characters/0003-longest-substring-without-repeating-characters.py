class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0
        seen = set()
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[i])
            ans = max(ans, i - left + 1)
        return ans



        