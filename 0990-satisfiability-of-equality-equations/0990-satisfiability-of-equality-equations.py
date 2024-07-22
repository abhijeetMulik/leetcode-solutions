class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = [i for i in range(26)]
        def find(x):
            print(x)
            if parent[x] != x:
                return find(parent[x])
            else:
                return x
        
        for eq in equations:
            if eq[1] == '=':
                parent[find(ord(eq[3]) - ord('a'))] = find(ord(eq[0]) - ord('a'))
    
        for eq in equations:
            if eq[1] == '!':
                if find(ord(eq[0]) - ord('a')) == find(ord(eq[3]) - ord('a')):
                    return False
        return True