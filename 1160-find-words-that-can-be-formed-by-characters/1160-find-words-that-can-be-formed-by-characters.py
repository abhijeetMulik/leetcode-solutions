class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            tmp = list(chars)
            count = 0
            for w in word:
                if w in tmp:
                    tmp.remove(w)
                    count += 1
                else:
                    break
            if count == len(word):
                ans += len(word)
        
        return ans
        