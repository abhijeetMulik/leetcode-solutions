class Solution:
    def simplifyPath(self, path: str) -> str:
        p = path.split('/')
        stack = []
        for i in p:
            if i != '.' and i != '' and i != '..':
                stack.append(i)
            if stack and i == '..':
                stack.pop()
        return '/' + "/".join(stack)


                


            
        