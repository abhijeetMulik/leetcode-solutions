class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = list(t)
        if len(s) != len(t):
            return False
        for i in s:
            if i not in temp:
                return False
            else:
                temp.remove(i)
        return True


        