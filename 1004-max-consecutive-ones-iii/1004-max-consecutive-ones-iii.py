class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr, ans, left = 0, 0, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                curr += 1
            while curr > k:
                if nums[left] == 0:
                    curr -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans
