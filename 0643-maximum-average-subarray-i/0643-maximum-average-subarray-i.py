class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = ans = cur_sum = 0

        for right in range(k):
            cur_sum += nums[right]
        
        ans = cur_sum / k
        for right in range(k, len(nums)):
            cur_sum += nums[right] - nums[left]
            left += 1
            ans = max(ans, cur_sum / k)
    
        return ans
