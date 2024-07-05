class RecentCounter:

    def __init__(self):
        self.count = 0
        self.queue = deque()
        

    def ping(self, t: int) -> int:
        self.count = 0
        self.queue.append(t)
        left_range = t - 3000
        # print('left range ->', left_range)
        # print('queue is ----> ',self.queue)
        for q in self.queue:
            # print('q. ->', q)
            if q >= left_range and q <= t:
                self.count += 1
        return self.count

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)