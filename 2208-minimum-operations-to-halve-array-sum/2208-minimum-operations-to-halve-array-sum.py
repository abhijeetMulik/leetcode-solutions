class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        target = sum(nums) / 2
        count, total = 0, 0
        

        while total < target:
            x = -heapq.heappop(heap)
            y = x / 2
            total += y
            heapq.heappush(heap, -y)
            count += 1
        
        return count
        

        