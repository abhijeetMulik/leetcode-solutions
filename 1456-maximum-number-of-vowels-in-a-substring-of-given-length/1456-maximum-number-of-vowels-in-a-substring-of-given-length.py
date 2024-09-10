class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = curr = ans = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for right in range(len(s)):
            if s[right] in vowels:
                curr += 1
            if right - left + 1 > k:
                if s[left] in vowels:
                    curr -= 1
                left += 1
            ans = max(ans, curr)
        return ans
                


        