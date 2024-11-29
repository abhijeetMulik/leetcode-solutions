class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        count = dict(sorted(count.items(), reverse = True))
        res = []
        for c, val in count.items():
            limit = val // 2
            if limit > 0:
                res.append(str(c) * limit)
                val -= (limit * 2)
                count[c] = val
        res = ''.join(res)
        mid = ''
        for k, v in count.items():
            if v == 1:
                mid = k
                break
        result = res + mid + res[::-1]
        result = result.strip('0') 
        # res = result[:-1]
        return result if len(result) > 0 else "0"

        