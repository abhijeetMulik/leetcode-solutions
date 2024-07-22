class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-p for p in piles]
        heapq.heapify(piles)

        for i in range(k):
            maxElement = abs(heapq.heappop(piles))
            heapq.heappush(piles, -ceil(maxElement/2))
        # print(piles)

        return -sum(piles)
        