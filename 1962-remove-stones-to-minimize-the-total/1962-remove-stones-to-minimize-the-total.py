class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [ -p for p in piles]
        heapq.heapify(heap)

        for i in range(k):
            x = -heapq.heappop(heap)
            heapq.heappush(heap, -ceil(x/2))
        

        return -sum(heap)
        