class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            '(' : ')',
            '[' :']',
            '{' : '}'
        }
        stack = []
        for c in s:
            if c in mappings:
                stack.append(c)
            else:
                if not stack:
                    return False
                removed = stack.pop()
                if mappings[removed] != c:
                    return False
        return not stack


        