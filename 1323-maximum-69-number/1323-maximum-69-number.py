class Solution:
    def maximum69Number (self, num: int) -> int:
        high = num
        nums = str(num)
        n = len(nums)
        for i in range(n):
            tmp = list(nums)
            if nums[i] == '9':
                tmp[i] = '6'
            else:
                tmp[i] = '9'
            if int("".join(tmp)) > high:
                high = int("".join(tmp))
        return high


        