class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        s1 = s.split(' ')
        for words in s1:
            ans.append(words[::-1])
        return ' '.join(ans)

