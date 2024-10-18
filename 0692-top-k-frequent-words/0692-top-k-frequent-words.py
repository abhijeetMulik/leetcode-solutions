class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hmap = Counter(words)
        res = []
        heap = []

        for key, val in hmap.items():
            heapq.heappush(heap, (-val, key))
        
        # print(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res


