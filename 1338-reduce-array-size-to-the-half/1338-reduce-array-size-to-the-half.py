class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        count = dict(sorted(count.items(), key = lambda x : x[1], reverse = True))
        n = len(arr)
        goal = n // 2
        # arr = set(arr)
        ans = 0

        for key in count:
            if n <= goal :
                break
            n -= count[key]
            ans += 1

        return ans
        