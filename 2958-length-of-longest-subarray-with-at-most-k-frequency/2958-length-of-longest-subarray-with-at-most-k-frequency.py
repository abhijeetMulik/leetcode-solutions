class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        ans = left = 0
        for right in range(len(nums)):
            dic[nums[right]] += 1
            while dic[nums[right]] > k:
                dic[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
        