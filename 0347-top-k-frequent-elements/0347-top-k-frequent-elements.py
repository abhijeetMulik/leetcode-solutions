class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for c in count:
            heapq.heappush(heap, (count[c],c))
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]


                
        
