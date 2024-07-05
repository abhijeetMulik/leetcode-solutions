class Solution:
    def removeStars(self, s: str) -> str:
        lis = []
        for i in s:
            if lis and i == '*':
                lis.pop()
            else:
                lis.append(i)
        return "".join(lis)

        