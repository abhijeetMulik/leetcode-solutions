class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        if not trust:
            if n == 1:
                return n
            else:
                return -1

        for i in trust:
            graph[i[0]].append(i[1])
        seen = set()
        for s in graph[trust[0][0]]:
            seen.add(s)
        if len(graph) != n - 1:
            return -1
        for n in graph:
            for t in graph[n]:
                if t not in seen:
                    print('discarded: ', t)
                    seen.discard(t)
        # print(seen)
        for judge in seen:
            if judge not in graph:
                return judge

        return -1
        