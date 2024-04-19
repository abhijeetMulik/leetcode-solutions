class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                res[r-l] = left * left
                l += 1
            else:
                res[r-l] = right * right
                r -= 1
        return res

        