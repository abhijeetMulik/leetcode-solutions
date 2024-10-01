class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter('balloon')
        string = Counter(text)

        ans = float('inf')

        for c in balloon:
            ans = min(ans, string[c] // balloon[c])

        return ans
