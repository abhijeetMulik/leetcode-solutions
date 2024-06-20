class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = 99999
        curr = left = 0
        for right in range(len(nums)):
            curr += nums[right]

            while curr >= target:
                ans = min(ans, right - left + 1)
                curr -= nums[left]
                left += 1
            
        if ans == 99999:
            return 0    
        return ans
        