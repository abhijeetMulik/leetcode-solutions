class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = []
        my_map = {}
        for i in range(len(s)):
            limit = i + 10
            if limit <= len(s):
                substr = s[i:limit]
                my_map[substr] = 1 + my_map.get(substr, 0)
        for k, v in my_map.items():
            if v >= 2:
                result.append(k)
        return result

        