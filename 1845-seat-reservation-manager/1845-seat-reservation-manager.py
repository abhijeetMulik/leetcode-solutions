class SeatManager:

    def __init__(self, n: int):
        self.heap = []
        self.count = 0
        

    def reserve(self) -> int:
        if not self.heap:
            self.count += 1
            return self.count
        return heapq.heappop(self.heap)
        

    def unreserve(self, seatNumber: int) -> None:
        if seatNumber == self.count:
            self.count -= 1
        else:
            heapq.heappush(self.heap, seatNumber)
        
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)