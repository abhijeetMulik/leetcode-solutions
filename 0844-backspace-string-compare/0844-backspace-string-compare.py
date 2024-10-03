class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def compare(input: str) -> str:
            stack = []
            for i in input:
                if i != '#':
                    stack.append(i)
                elif stack and i == '#':
                    stack.pop()
            
            return ''.join(stack)
        
        return compare(s) == compare(t)


        