class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        for i in range(len(bombs)):
            for j in range(1 + i, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                if d <= r1:
                    graph[i].append(j)
                if d <= r2:
                    graph[j].append(i)
        
        def bfs(index):
            q = deque([(index)])
            seen = {i}
            while q:
                curr = q.popleft() # index
                for neighbor in graph[curr]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        q.append(neighbor)
            return len(seen)
        
        res = 0
        for i in range(len(bombs)):
            res = max(res, bfs(i)) #bfs(i)
        return res
            
            