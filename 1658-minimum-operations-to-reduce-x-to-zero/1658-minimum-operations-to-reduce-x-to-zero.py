class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        targetToFind = sum(nums) - x
        if targetToFind < 0:
            return -1
        left = curr = 0
        ans = float('inf')
        for right in range(len(nums)):
            curr += nums[right]
            while curr > targetToFind and left < len(nums):
                curr -= nums[left]
                left += 1
            if curr == targetToFind:
                ans = min(ans, len(nums) - (right - left + 1))
        return ans if ans != float('inf') else -1
        
        