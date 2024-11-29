class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        dic = defaultdict(int)
        for i in range(26):
            dic[i + 1] = chr(ord('a') + i)
        res = ['a'] * n
        for i in range(n, 0, -1):
            limit = k - (i - 1)
            if limit > 26:
                res[i - 1] = 'z'
                k -= 26
            else:
                res[i - 1] = chr(ord('a') + limit - 1)
                k -= limit

        return ''.join(res)
