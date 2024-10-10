class LRUCache:

    def __init__(self, capacity: int):
        self.hmap = defaultdict(int)
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.hmap:
            ans = self.hmap[key]
            del self.hmap[key]
            self.hmap[key] = ans
            return ans
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        res = self.get(key)
        if res < 0 and len(self.hmap) + 1 > self.capacity:
            first_key = next(iter(self.hmap))
            del self.hmap[first_key]
        self.hmap[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)