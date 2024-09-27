class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')  
        if len(pattern)  != len(s):
            return False
        dic = defaultdict(str)          
        for i in range(len(pattern)):
            if pattern[i] not in dic and s[i] not in dic.values():
                dic[pattern[i]] = s[i]
            elif pattern[i] in dic:
                if dic[pattern[i]] != s[i]:
                    return False
            elif s[i] in dic.values():
                return False

        return True