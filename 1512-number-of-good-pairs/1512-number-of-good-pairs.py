class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        for k, v in count.items():
            if v > 1:
                ans += v * (v - 1) // 2
        return ans
        