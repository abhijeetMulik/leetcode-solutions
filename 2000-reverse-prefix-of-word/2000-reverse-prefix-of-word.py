class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        slist = list(word)
        if ch not in slist:
            return word
        left = 0
        right = slist.index(ch)
        while left <= right:
            slist[left], slist[right] = slist[right], slist[left]
            left += 1
            right -= 1
        return "".join(slist)
        
        