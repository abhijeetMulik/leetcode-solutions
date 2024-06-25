class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for i in sentence:
            seen.add(i)
        return len(seen) == 26
        