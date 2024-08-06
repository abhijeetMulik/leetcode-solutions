class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            idx = nums.index(min(nums))
            nums[idx] *= -1
        return sum(nums)
        