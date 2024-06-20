class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr = 0
        left = 0
        ans = 999999
        for i in range(len(nums)):
            curr += nums[i]
            while curr >= target:
                ans = min(ans, i - left + 1)
                curr -= nums[left]
                left += 1
        if ans == 999999:
            return 0
        return ans
        