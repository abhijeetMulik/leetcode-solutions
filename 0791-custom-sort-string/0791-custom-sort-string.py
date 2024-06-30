class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = []
        tmp = list(s)
        for i in order:
            while i in tmp:
                ans.append(i)
                tmp.remove(i)
        # print(sorted(tmp))
        tmp = sorted(tmp)
        for i in tmp:
            ans.append(i)
        # print('--> 2 ', tmp)
        return ''.join(ans)
        