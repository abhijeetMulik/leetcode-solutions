class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        n = len(nums)
        res = [-1] * n
        window_size = 2 * k + 1

        if window_size > n:
            return res

        window_sum = sum(nums[:window_size])
        res[k] = window_sum // window_size

        for i in range(window_size, n):
            window_sum = window_sum - nums[i-window_size] + nums[i]
            res[i-k] = window_sum // window_size
        return res

        