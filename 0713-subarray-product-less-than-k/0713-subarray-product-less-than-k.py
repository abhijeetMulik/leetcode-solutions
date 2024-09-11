class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = left = 0
        curr = 1
        if k <= 0:
            return ans
        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                if left >= len(nums):
                    return ans if ans >= 0 else 0
                curr /= nums[left]
                left += 1
            
            ans += right - left + 1
        
        return ans if ans >= 0 else 0
