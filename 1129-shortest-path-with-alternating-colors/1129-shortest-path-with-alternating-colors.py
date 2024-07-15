class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for src, dst in redEdges:
            red[src].append(dst)
        
        for src, dst in blueEdges:
            blue[src].append(dst)

        q = deque() 
        q.append([0, 0, None])# node, length, color_of_previous_edge
        seen = set()
        seen.add((0, None)) #node, color_of_previous_edge
        answer = [-1] * n

        while q:
            node, length, edgeColor = q.popleft()
            if answer[node] == -1:
                answer[node] = length
            
            if edgeColor is not "RED":
                for neighbour in red[node]:
                    if (neighbour, "RED") not in seen:
                        seen.add((neighbour, "RED"))
                        q.append([neighbour, length + 1, "RED"])

            if edgeColor is not "BLUE":
                for neighbour in blue[node]:
                    if (neighbour, "BLUE") not in seen:
                        seen.add((neighbour, "BLUE"))
                        q.append([neighbour, length + 1, "BLUE"])
        return answer


        