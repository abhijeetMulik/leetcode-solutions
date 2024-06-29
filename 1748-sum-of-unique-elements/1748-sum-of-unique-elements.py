class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = sum(nums)
        for k, v in count.items():
            if v > 1:
                ans -= (k*v)
        return ans
        