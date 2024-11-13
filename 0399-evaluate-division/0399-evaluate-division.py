class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def helper(start, end):
            if start not in graph:
                return -1
            
            seen = {(start)}
            stack = [(start, 1)] # start, ratio

            while stack:
                node, ratio = stack.pop()

                if node == end:
                    return ratio
                
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor, ratio * graph[node][neighbor]))
            
            return -1
        
        graph = defaultdict(dict)
        for i in range(len(equations)):
            num, den = equations[i]
            val = values[i]
            graph[num][den] = val
            graph[den][num] = 1 / val
        
        ans = []
        for q in queries:
            ans.append(helper(q[0], q[1]))
        
        return ans

