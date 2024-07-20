class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        if len(roads) == 1:
            return 1

        for src, dst in roads:
            graph[src].append(dst)
            graph[dst].append(src)
        print(graph)

        def countNetwork(r0, r1):
            seen = list()
            for r in [r0, r1]:
                seen.extend(graph[r])
            if r0 in seen:
                seen.remove(r0)
            elif r1 in seen:
                seen.remove(r1)
            # print(road[0])
            return len(seen)
                

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                ans = max(ans, countNetwork(i, j))

        return ans
        