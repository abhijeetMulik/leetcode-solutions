class Solution:
    def minOperations(self, s: str) -> int:
        dx, dy = [], []
        ans = 0
        for i in range(len(s)):
            if i % 2 == 0:
                dx.append('0')
                dy.append('1')
            else:
                dx.append('1')
                dy.append('0')

        # start with 0
        for i in range(len(s)):
            if s[i] != dx[i]:
                ans += 1

        ans = min(ans, len(s) - ans)

        # start with 1


        return ans