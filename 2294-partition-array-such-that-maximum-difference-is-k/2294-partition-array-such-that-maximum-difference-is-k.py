class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        x = nums[0]
        ans = []
        a = []
        for n in nums:
            if abs(n - x) <= k:
                a.append(n)
            else:
                ans.append(a)
                x = n
                a = []
                a.append(n)
        ans.append(a)
        return len(ans)
        