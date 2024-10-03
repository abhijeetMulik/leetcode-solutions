class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        if len(s) % 2 == 1:
            return False 
        
        stack = []
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if not stack or i != dic[stack.pop()]:
                    return False
        return not stack
