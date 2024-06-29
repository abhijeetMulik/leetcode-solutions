class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n == 1:
            return s1 in s2
        s11 = sorted(s1)
        for i in range(0,len(s2) - n + 1):
            if sorted(s2[i:i+n]) == s11:
                return True
        return False


        