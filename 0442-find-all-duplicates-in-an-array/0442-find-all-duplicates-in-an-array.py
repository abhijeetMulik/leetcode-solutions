class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []

        for n in nums:
            indx = abs(n) - 1
            if nums[indx] < 0:
                ans.append(abs(indx) + 1)
            else:
                nums[indx] = -nums[indx]
        return ans

        