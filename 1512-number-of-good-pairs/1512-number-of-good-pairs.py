class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 1):
            tmp = nums[i+1:]
            for j in range(len(tmp)):
                if nums[i] == tmp[j]:
                    ans += 1
        return ans
        