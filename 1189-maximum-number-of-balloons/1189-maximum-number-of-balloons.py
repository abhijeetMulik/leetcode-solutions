class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        balloon = Counter("balloon")
        result = len(text)
        for i in balloon:
            result = (min(result, count[i]//balloon[i]))
        return result
        
        
