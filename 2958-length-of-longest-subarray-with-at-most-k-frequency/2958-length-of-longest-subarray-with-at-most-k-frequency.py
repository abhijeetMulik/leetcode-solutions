class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left, ans = 0, 0
        dic = defaultdict(int)
        for i, n in enumerate(nums):
            dic[n] += 1
            while dic[n] > k:
                dic[nums[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)
        return ans