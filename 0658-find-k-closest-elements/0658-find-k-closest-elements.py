class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for a in arr:
            heapq.heappush(heap, (-abs(a - x), -a))
            if len(heap) > k:
                heapq.heappop(heap)
        return sorted([ -h[1] for h in heap])