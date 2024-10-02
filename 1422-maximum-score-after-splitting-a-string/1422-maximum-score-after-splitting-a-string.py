class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 1):
            left = s[: i + 1]
            right = s[i + 1 :]
            ans = max(ans, left.count('0') + right.count('1'))
        
        return ans

        