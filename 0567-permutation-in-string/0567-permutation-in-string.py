class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n == 1:
            return s1 in s2
        count_s1 = Counter(s1)
        for i in range(0, len(s2) - n + 1):
            if Counter(s2[i : i + n]) == count_s1:
                return True
        return False
            



        