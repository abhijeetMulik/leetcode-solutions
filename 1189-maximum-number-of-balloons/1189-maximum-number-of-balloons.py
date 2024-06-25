class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter('balloon')
        count = Counter(text)
        result = float('inf')
        for i in balloon:
            result = min(result, count[i]//balloon[i])
        return result