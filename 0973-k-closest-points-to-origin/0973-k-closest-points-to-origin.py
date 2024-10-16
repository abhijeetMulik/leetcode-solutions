class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        
        for p in points:
            euc = (p[0]) ** 2 + (p[1]) ** 2
            heapq.heappush(heap, (sqrt(euc), p))
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res

        