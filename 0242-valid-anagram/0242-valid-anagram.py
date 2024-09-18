class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)
        count2 = Counter(t)
        return count == count2
        