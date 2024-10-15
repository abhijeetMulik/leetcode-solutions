class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        total = 0
        for i in range(len(nums)):
            if total < 0:
                total = 0
            
            total += nums[i]
            
            ans = max(ans, total)
        
        return ans
            
        