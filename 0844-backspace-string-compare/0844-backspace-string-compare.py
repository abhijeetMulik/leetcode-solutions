class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def compare(s):
            stack = []
            for c in s:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return "".join(stack)
        
        return compare(s) == compare(t)