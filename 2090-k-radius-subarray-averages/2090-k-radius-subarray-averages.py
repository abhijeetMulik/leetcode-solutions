class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        if k == 0:
            return nums
        ans = [-1] * len(nums)
        limit = k+k+1
        
        if limit > len(nums):
            return ans

       

        

        init_sum = sum(nums[:limit])

        ans[k] = init_sum // limit

        for right in range(limit, len(nums)):
            init_sum += nums[right] - nums[right - limit]
            ans[right - k] = init_sum // limit

        return ans

        