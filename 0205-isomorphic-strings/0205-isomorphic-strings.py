class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = defaultdict(str)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dic and t[i] not in dic.values():
                print(s[i])
                dic[s[i]] = t[i]
            else:
                if dic[s[i]] != t[i]:
                    return False
        return True





        