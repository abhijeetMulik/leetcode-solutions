class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum, count = 0,0
        sum_map = {0 : 1}

        for i in nums:
            sum += i
            complement = sum - k
            if complement in sum_map:
                count+= sum_map[complement]
            sum_map[sum] = sum_map.get(sum, 0) + 1
        return count
        