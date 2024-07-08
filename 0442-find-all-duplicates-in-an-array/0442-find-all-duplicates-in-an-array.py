class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for i, n in enumerate(nums):
            indx = abs(n) - 1
            if nums[indx] < 0 and nums[indx] not in ans:
                ans.append(abs(indx) + 1)
            else:
                nums[indx] = -nums[indx]
        return ans

        