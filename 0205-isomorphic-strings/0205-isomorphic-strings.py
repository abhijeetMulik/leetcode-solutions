class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        if len(s) != len(t):
            return False
        for i,n in enumerate(s):
            if n in dic :
                if dic[n] != t[i]:
                    return False
            else:
                if t[i] in dic.values():
                    return False
            dic[n] = t[i]
        return True


        