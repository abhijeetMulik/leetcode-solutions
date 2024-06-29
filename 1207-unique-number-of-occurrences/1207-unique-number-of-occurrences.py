class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = Counter(arr)
        seen = set()
        for k in dic:
            if dic[k] in seen:
                return False
            else:
                seen.add(dic[k])
        return True

        