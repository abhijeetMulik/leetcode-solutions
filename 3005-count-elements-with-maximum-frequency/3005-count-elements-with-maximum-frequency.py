class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        n = max(count.values())
        for i in count.values():
            if i == n:
                ans += i
        return ans

        