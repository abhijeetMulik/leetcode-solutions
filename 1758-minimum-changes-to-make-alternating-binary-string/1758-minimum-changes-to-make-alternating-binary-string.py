class Solution:
    def minOperations(self, s: str) -> int:
        res = float('inf')

        # start with 0
        ans = 0
        for i in range(len(s)):
            if(i % 2 == 0 and s[i] == '1'): 
                print('s[i] :', s[i], 'i: ', i)
                ans += 1
            elif (i % 2 == 1 and s[i] == '0'):
                print('s[i] :', s[i], 'i: ', i)
                ans += 1
        res = min(res, ans)

        # start with 1
        ans = 0
        for i in range(len(s)):
            if  (i % 2 == 0 and s[i] == '0'):
                ans += 1
            elif (i % 2 == 1 and s[i] == '1'):
                ans += 1
        res = min(res, ans)

        return res