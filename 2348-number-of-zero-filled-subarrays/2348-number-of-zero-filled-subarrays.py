class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result =0
        count =0
        for z in nums:
            if z ==0:
                count +=1
            else:
                count = 0
            result +=count
        return result