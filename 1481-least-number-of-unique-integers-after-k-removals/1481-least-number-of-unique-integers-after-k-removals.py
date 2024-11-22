class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dic = Counter(arr)
        heap = []
        for key, val in dic.items():
            heapq.heappush(heap, (val, key))
        
        for _ in range(k):
            ele = heapq.heappop(heap)
            if ele[0] > 1:
                heapq.heappush(heap, (ele[0] - 1, ele[1]))
        
        return len(heap)