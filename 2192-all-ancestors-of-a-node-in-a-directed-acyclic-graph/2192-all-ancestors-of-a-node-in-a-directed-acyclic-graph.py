class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        for src, dst in edges:
            graph[src].append(dst)
            indegree[dst] += 1

        # print(graph)
        # print(indegree)

        # topological sort
        topo_sort = []
        q = deque([i for i in range(n) if indegree[i] == 0])
        # print(q)
        while q:
            node = q.popleft()
            topo_sort.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        ancestors = [set() for i in range(n)]
        
        for node in topo_sort:
            for neighbor in graph[node]:
                ancestors[neighbor].add(node)
                ancestors[neighbor].update(ancestors[node])
        result = [ sorted(list(a)) for a in ancestors]
        return result
