class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.de = deque()
        self.total = 0
        

    def next(self, val: int) -> float:
        self.de.append(val)
        if len(self.de) > self.size:
            self.total -= self.de[0]
            self.de.popleft()
        self.total += val
        return self.total / len(self.de)

        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)