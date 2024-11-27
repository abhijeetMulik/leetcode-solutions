class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        ans = 0
        for n in s:
            if n not in seen:
                seen.add(n)
            else:
                seen.clear()
                seen.add(n)
                ans += 1
        
        return ans + 1 if len(seen) > 0 else ans
        