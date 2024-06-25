class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0

        for c in count.keys():
            if count[c] == 1:
                ans = max(ans, c)
        return -1 if ans == 0 else ans

        