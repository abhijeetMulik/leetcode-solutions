class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        heap = []
        for b in boxTypes:
            heapq.heappush(heap, (-b[1], b[0]))
        # print(heap)

        while truckSize > 0 and heap:
            unit, box = heapq.heappop(heap)
            if box <= truckSize:
                ans += (box * -(unit))
            else:
                ans += (truckSize * -(unit))
            truckSize -= box

        return ans

        