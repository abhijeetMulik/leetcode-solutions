class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen = {}
        for p in paths:
            seen[p[0]] = p[1]

        for val in seen.values():
            if val not in seen:
                return val
        