class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        myMap = {}
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in myMap:
                if s[i] in myMap.values():
                    return False
                myMap[pattern[i]] =s[i]
            elif myMap[pattern[i]] != s[i]:
                return False
        return True
        