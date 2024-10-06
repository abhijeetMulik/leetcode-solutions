class Solution:
    def robotWithString(self, s: str) -> str:
        paper = []
        t = []
        min_stack = ['z'] * (len(s) + 1)

        for i in range(len(s) - 1, -1, -1):
            min_stack[i] = min(min_stack[i + 1], s[i])
        
        for i in range(len(s)):
            t.append(s[i])
            while t and t[-1] <= min_stack[i + 1]:
                paper.append(t.pop())


        return ''.join(paper)

        