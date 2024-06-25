class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = Counter(text)
        default = Counter("balloon")
        ans = float('inf')

        for key in default.keys():
            ans = min(ans, c[key]//default[key])

        return ans
