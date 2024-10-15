class MedianFinder:

    def __init__(self):
        self.min_heap = [] # max heap for large
        self.max_heap = [] # min heap for small

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, -num)
        # print('initial min: ', self.min_heap)

        if self.min_heap and self.max_heap and -self.min_heap[0] > self.max_heap[0]:
            x = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -x)
        
        if len(self.min_heap) > len(self.max_heap) + 1:
            x = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -x)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            x = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -x)
        
        # print('min: ', self.min_heap)
        # print('max: ',self.max_heap)


    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return -self.min_heap[0]
        
        if len(self.max_heap) > len(self.min_heap):
            return self.max_heap[0]
        
        
        return (-self.min_heap[0] + self.max_heap[0]) / 2
        



        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()