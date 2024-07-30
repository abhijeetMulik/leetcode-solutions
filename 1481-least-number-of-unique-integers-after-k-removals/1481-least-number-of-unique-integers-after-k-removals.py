class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        # print('count:', count)
        heap = []
        for v in count:
            heapq.heappush(heap, (count[v], v))
        # print('heap: ',heap)
        for i in range(k):
            val, key = heapq.heappop(heap)
            # print('key, val :', key, ' ', val)
            if val > 1:
                heapq.heappush(heap, (val - 1, key))
        # print(heap)
        return len(heap)
