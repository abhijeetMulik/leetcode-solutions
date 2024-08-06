class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        dic = defaultdict(int)
        count = 0
        for a in range(1, 27):
            dic[a] = chr(count + ord('a'))
            count += 1
        ans = []
        for i in range(n, 0, -1):
            limit = k - (i - 1)
            if limit > 26:
                ans.append('z')
                k -= 26
            else:
                ans.append(dic[limit])
                k -= limit 
        return ''.join(sorted(ans))

        