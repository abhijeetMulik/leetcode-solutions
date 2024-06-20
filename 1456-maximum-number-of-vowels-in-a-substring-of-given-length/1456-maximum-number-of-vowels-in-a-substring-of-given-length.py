class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = ans = temp = 0
        v = ['a', 'e', 'i', 'o', 'u']
        for right in range(len(s)):
            if s[right] in v:
                temp += 1
            if right - left + 1 > k:
                if s[left] in v:
                    temp -= 1
                left += 1
            ans = max(ans, temp)
        return ans
        