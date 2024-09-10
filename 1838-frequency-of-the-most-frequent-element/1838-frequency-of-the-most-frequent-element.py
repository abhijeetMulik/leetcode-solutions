class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        right = 0
        curr = 0
        ans = 0 
        left = 0
        while right < len(nums):
            curr += nums[right]
            while nums[right] * (right - left + 1) > curr + k:
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
            
        return ans
       
        