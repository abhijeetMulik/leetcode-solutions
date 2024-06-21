class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = curr = ans = 0
        for right in range(len(s)):
            curr += abs(ord(s[right]) - ord(t[right]))
            
            while curr > maxCost:
                curr -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            ans = max(ans, right - left + 1)
        return ans
        