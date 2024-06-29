class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        def helper(goal):
            if goal < 0:
                return 0

            curr = ans = left = 0
            for i in range(len(nums)):
                curr += nums[i]
                while curr > goal:
                    curr -= nums[left]
                    left += 1
                ans += i - left + 1
            return ans


        return helper(goal) - helper(goal - 1)
