class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        max_ele, ans = nums[0], 0
        for n in nums:
            if max_ele - n > k:
                ans += 1
                max_ele = n

        return ans + 1

        