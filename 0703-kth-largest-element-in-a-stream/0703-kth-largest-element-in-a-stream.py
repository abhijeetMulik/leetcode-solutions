class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums #[-n for n in nums]
        heapq.heapify(self.nums)
        self.k = k
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heappushpop(self.nums, val)
        return self.nums[0]
        # k_largest = heapq.nlargest(self.k, self.nums)
        # return k_largest[-1]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)