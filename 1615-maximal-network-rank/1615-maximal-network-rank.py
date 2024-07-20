class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Calculate degree of each city
        degree = [0] * n
        connected = defaultdict(set)

        for src, dst in roads:
            degree[src] += 1
            degree[dst] += 1
            connected[src].add(dst)
            connected[dst].add(src)
        
        # Step 2: Calculate the maximal network rank
        max_rank = 0

        for i in range(n):
            for j in range(i + 1, n):
                # Calculate the network rank of cities i and j
                rank = degree[i] + degree[j]
                if j in connected[i]:  # If i and j share a direct road, subtract one
                    rank -= 1
                max_rank = max(max_rank, rank)
        
        return max_rank








        # graph = defaultdict(list)
        # if len(roads) == 1:
        #     return 1

        # for src, dst in roads:
        #     graph[src].append(dst)
        #     graph[dst].append(src)

        # def countNetwork(r0, r1):
        #     seen = list()
        #     for r in [r0, r1]:
        #         seen.extend(graph[r])
        #     if r0 in seen:
        #         seen.remove(r0)
        #     elif r1 in seen:
        #         seen.remove(r1)
        #     return len(seen)
                

        # ans = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         ans = max(ans, countNetwork(i, j))

        # return ans
        