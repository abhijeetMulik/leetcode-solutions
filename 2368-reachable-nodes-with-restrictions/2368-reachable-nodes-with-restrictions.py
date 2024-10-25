class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        def dfs(node):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen and neighbor not in restricted:
                    dfs(neighbor)

        graph = defaultdict(list)
        seen = set()
        restricted = set(restricted)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        dfs(0)

        return len(seen)