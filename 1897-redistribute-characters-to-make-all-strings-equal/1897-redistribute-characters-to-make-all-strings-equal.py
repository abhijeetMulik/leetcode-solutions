class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = defaultdict(int)

        for word in words:
            for w in word:
                count[w] += 1
        
        for c in count:
            if count[c] % len(words) != 0:
                return False
        
        return True
        