class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.removed = []
        self.smallest = 1
        

    def popSmallest(self) -> int:
        if self.removed:
            small = heapq.heappop(self.removed)
        else:
            heapq.heappush(self.heap, self.smallest)
            small = self.smallest
            self.smallest += 1
        return small

    def addBack(self, num: int) -> None:
        print(num)
        if self.heap and num == self.heap[0]:
            heapq.heappush(self.removed, heapq.heappop(self.heap))

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)