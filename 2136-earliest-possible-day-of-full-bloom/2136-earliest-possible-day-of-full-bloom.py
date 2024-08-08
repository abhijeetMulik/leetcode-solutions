class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        planted = sorted(zip(plantTime, growTime), key = lambda x:x[1], reverse = True)
        bloomed = 0
        totalDays = 0

        for p, g in planted:
            totalDays += p
            bloomed = max(bloomed, totalDays + g)

        return bloomed


            