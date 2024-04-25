class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        i = 0
        startval = 1
        temp = startval
        while i <= len(nums)-1:
            startval += nums[i]
            i += 1
            if startval < 1:
                temp += 1
                startval = temp
                i = 0
        return temp

        