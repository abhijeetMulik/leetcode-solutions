class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count = defaultdict(list)
        ans = float('-inf')
        for c in range(len(s)):
            count[s[c]].append(c)

        for c in count:
            if len(count[c]) > 1:
                val = sorted(count[c])
                ans = max(ans, val[-1] - val[0] - 1)

        return ans if ans != float('-inf') else -1