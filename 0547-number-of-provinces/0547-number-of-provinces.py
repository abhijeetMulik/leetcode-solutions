class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node, visited):
            visited[node] = True
            for j in range(len(isConnected)):
                if isConnected[node][j] == 1 and not visited[j]: 
                    dfs(j, visited)

        n = len(isConnected)
        visited = [False] * n
        province = 0

        for i in range(n):
            if not visited[i]:
                dfs(i, visited)
                province += 1
        
        return province
        