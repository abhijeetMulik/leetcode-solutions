class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr, average = 0, 0
        
        
        for i in range(k):
            curr += nums[i]
        average = curr / k
        
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i-k]
            average = max(average, curr/k)
        return average