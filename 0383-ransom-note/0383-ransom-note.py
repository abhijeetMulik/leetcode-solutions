class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = defaultdict(int)
        for m in magazine:
            mag[m] += 1
        for i in ransomNote:
            if i in mag:
                mag[i] -= 1
            else:
                return False
            if mag[i] == 0:
                del mag[i]
        return True
            
        