class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        left = 0
        for i in range(len(nums)):
            right = totalSum - nums[i] - left
            if left == right:
                return i
            left += nums[i]
        return -1
