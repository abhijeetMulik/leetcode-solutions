class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for c in count:
            heapq.heappush(heap, (-count[c], c))
        # print('heap :', heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]