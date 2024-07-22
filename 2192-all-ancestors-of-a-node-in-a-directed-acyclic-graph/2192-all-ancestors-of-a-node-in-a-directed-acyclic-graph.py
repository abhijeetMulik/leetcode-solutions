class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Step 1: Create the graph and indegree array
        graph = defaultdict(list)
        indegree = [0] * n
        for src, dst in edges:
            graph[src].append(dst)
            indegree[dst] += 1
        
        # Step 2: Perform topological sort using a deque
        topo_sort = []
        queue = deque([i for i in range(n) if indegree[i] == 0])
        
        while queue:
            node = queue.popleft()
            topo_sort.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 3: Propagate ancestor information
        ancestors = [set() for _ in range(n)]
        
        for node in topo_sort:
            for neighbor in graph[node]:
                # Add the current node to the neighbor's ancestor set
                ancestors[neighbor].add(node)
                # Add all ancestors of the current node to the neighbor's ancestor set
                ancestors[neighbor].update(ancestors[node])
        
        # Step 4: Convert sets to sorted lists
        result = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
        
        return result