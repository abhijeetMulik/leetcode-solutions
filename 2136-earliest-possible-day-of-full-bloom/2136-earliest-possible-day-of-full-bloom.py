class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        planted = sorted(zip(plantTime, growTime), key = lambda a : a[1], reverse = True)
        days = 0
        result = 0
        for p, g in planted:
            days += p
            result = max(result, days + g)
        return result
        