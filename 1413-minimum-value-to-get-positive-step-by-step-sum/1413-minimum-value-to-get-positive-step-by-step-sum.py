class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = minVal = 0

        for i in nums:
            total += i
            minVal = min(minVal, total)
        
        return -minVal + 1

            

        