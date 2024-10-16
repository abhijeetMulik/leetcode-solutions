class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) <= 1:
            return 0
        
        heapq.heapify(sticks)
        total = 0

        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            tmp = first + second
            total += tmp
            heapq.heappush(sticks, tmp)
        
        return total