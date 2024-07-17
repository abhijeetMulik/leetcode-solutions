class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(dict)
        for i in range(len(equations)):
            n, d = equations[i]
            val = values[i]
            graph[n][d] = val
            graph[d][n] = 1 / val
            

        def find_ans(start, end):
            if start not in graph:
                return -1
            
            seen = {start}
            stack = [(start, 1)] 

            while stack:
                node, steps = stack.pop()
                if node == end:
                    return steps
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append((neighbor, steps * graph[node][neighbor]))
            return -1
                
        ans = []
        for n, d in queries:
            ans.append(find_ans(n, d))
        return ans

        