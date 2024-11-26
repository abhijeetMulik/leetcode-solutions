class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        
        for _ in range(k):
            low = min(nums)
            nums[nums.index(low)] = -low
        
        return sum(nums)

        