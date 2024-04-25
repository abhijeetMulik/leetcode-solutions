class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        ans,left = 0,0
        curr = 1

        for i in range(len(nums)):
            curr *= nums[i]
            while curr >= k:
                curr //= nums[left]
                left += 1
            ans += i - left + 1
        return ans
        