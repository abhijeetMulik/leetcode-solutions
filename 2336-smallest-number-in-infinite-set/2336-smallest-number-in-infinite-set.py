class SmallestInfiniteSet:

    def __init__(self):
        self.list = list()
        self.heap = []
        self.smallest = 1
        

    def popSmallest(self) -> int:
        if self.heap:
            small = heapq.heappop(self.heap)
            self.list.append(small)
        else:
            self.list.append(self.smallest)
            small = self.smallest
            self.smallest += 1
        return small

    def addBack(self, num: int) -> None:
        if num in self.list:
            heapq.heappush(self.heap, num)
            self.list.remove(num)


        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)