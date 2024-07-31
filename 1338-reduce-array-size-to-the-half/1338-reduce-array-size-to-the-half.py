class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        count = dict(sorted(count.items(), key = lambda x : x[1], reverse = True))
        n = len(arr)
        goal = len(count) // 2
        arr = set(arr)

        for key in count:
            if (n <= goal) or (n - count[key] < goal):
                break
            n -= count[key]
            arr.discard(key)

        return len(arr) if len(arr) > 0 else 1
        