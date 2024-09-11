class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for a in arr:
            distance = abs(a - x)
            heapq.heappush(heap, (-distance, -a))
            if len(heap) > k:
                heapq.heappop(heap)
        return sorted(-h[1] for h in heap)
