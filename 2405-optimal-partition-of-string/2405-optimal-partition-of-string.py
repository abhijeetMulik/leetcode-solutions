class Solution:
    def partitionString(self, s: str) -> int:
        result = []
        tmp =[]
        for c in s:
            if c not in tmp:
                tmp.append(c)
            else:
                result.append(tmp)
                tmp = [c]
        result.append(tmp)
        return len(result)
        