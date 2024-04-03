class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sorted_p = ''.join(sorted(p))
        result = []
        for i in range(len(s)-(len(p))+1):
            if ''.join(sorted(s[i:i+len(p)])) == sorted_p:
                result.append(i)
        return result