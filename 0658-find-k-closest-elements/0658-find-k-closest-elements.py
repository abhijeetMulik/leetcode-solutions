class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        res = []
        for a in arr:
            heapq.heappush(heap, ( abs(x - a), a))
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return sorted(res)
        