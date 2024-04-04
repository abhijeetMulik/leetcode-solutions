class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        my_map = {0 : -1}
        total = 0
        for i, n in enumerate(nums):
            total +=n
            rem = total % k
            if rem not in my_map:
                my_map[rem] = i
            elif i - my_map[rem] > 1:
                return True
        return False     

        # for i in range(len(nums)):
        #     total_sum = nums[i]
        #     for j in range(i+1, len(nums)):
        #         total_sum += nums[j]
        #         if (total_sum%k) == 0:
        #             return True
        # return False
            
        