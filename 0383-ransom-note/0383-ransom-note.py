class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)

        for k in ransomNote:
            if k in count:
                count[k] -= 1
                if count[k] == 0:
                    del count[k]
            else:
                return False
        return True
        