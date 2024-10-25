class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node):
            if node == destination:
                    return True
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor):
                        return True
            return False

        graph = defaultdict(list)
        seen = {0}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        
        
        return dfs(source)
            