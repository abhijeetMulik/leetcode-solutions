class Solution:
    def repeatedCharacter(self, s: str) -> str:
        lis = set()
        for i in s:
            if i in lis:
                return i
            lis.add(i)
        