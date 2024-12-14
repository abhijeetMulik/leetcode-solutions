class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1 

        while left <= right:
            m = (left + right) // 2
            if((m - 1 < 0 or nums[m - 1] != nums[m]) and (m + 1 >= len(nums) or nums[m + 1] != nums[m])):
                return nums[m]
            
            left_side = m - 1 if nums[m - 1] == nums[m] else m

            if left_side % 2:
                right = m - 1
            else:
                left = m + 1
        