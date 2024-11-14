class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        res = 0

        for r0, r1 in roads:
            graph[r0].add(r1)
            graph[r1].add(r0)

        for i in range(n):
            for j in range(i + 1, n):
                rank = len(graph[i]) + len(graph[j])
                if j in graph[i]:
                    rank -= 1
                res =  max(res, rank)
        
        return res