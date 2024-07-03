class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if stack:
                if stack[-1] != i and stack[-1].lower() == i.lower():
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        return "".join(stack)
        