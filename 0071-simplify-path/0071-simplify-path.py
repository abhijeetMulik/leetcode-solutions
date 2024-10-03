class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for p in path:
            if p and p != '..' and p != '.':
                stack.append(p)
            elif stack and p == '..':
                print('p is :', p)
                stack.pop()

        return '/' + '/'.join(stack)