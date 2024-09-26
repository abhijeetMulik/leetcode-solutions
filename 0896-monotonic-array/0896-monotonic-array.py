class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] - nums[-1] > 0:
            nums = nums[::-1]
        
        for n in range(len(nums) - 1):
            if nums[n] > nums[n + 1]:
                return False
        
        return True
