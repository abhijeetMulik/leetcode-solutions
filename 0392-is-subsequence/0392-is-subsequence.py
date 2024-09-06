class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        if len(s) < 1:
            return True
        for i in t:
            if i == s[j]:
                j += 1
            if j >= len(s):
                return True
        return False

            