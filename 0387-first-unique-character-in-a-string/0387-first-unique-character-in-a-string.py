class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = defaultdict(list)
        for i, v in enumerate(s):
            seen[v].append(i)
        
        for k in seen.values():
            if len(k) == 1:
                return k[0]
        return -1

