class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        self.seen = set()
        

    def popSmallest(self) -> int:
        small = heapq.heappop(self.heap)
        self.seen.add(small)
        return small
        

    def addBack(self, num: int) -> None:
        if num in self.seen:
            heapq.heappush(self.heap, num)
            self.seen.discard(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)