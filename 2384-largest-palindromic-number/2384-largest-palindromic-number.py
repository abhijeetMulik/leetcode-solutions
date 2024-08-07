class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        count = dict(sorted(count.items(), key = lambda x:x[0] ,reverse = True))
        # print(count)
        ans = []
        max_ele = -inf
        for c in count:
            if count[c] > 1:
                ans.append(c * (count[c]//2))
                if count[c] % 2:
                    count[c] -= round((count[c]/2))
                if count[c] % 2 == 0:
                    count[c] = 0
        # print(count)
        for i in count:
            if count[i] > 0:
                max_ele = i
                break
        x = []
        x.extend(ans)
        x.reverse()
        if max_ele != -inf:
            ans.append(str(max_ele))
        ans.extend(x)
        res = ''.join(ans).strip('0')
        return res if len(res) > 0 else "0"
        