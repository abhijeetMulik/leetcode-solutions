class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i in t:
                index = t.index(i)
                t = t[index+1:]
            else:
                return False
        return True
                
        