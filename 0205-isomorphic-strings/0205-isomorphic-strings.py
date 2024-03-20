class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        myMap = {}
        if len(s)!= len(t):
            return False
        for i in range(len(s)):
            if s[i] not in myMap:
                if t[i] in myMap.values():
                    return False
                myMap[s[i]] = t[i]
            elif myMap.get(s[i]) != t[i]:
                return False
        return True

            
                
            

        