class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        n = len(arr)
        count = dict(sorted(count.items(), key = lambda x :x[1], reverse = True))
        val = list(count.values())
        curr = 0
        ans = 0

        for left in range(n):
            curr += val[left]
            ans += 1
            if curr >= (n/2):
                break
        return ans
