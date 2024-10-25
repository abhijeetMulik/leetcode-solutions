class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def dfs(i, visited):
            visited[i] = True
            for j in graph[i]:
                if not visited[j]:
                    dfs(j, visited)

        visited = [False] * n
        graph = defaultdict(list)
        ans = 0
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        for i in range(n):
            if not visited[i]:
                dfs(i, visited)
                ans += 1
        
        return ans