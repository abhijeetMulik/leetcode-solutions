class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        seen = set(arr)
        for i in arr:
            if (i + 1) in seen:
                count += 1
        return count