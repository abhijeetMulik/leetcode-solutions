class Solution:
    def specialArray(self, nums: List[int]) -> int: 
        nums.sort()
        i = 0
        right = len(nums)
        prev = -1
        while i < len(nums):
            if nums[i] == right or prev < right < nums[i]:
                return right
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            prev = nums[i]
            i += 1
            right = len(nums) - i
        return -1
        
