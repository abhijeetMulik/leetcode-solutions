class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        count_max = 0
        for num in nums:
            if (num -1) not in numset:
                count = 1
                while (num+count) in numset:
                    count+=1
                count_max = max(count_max, count)
        return count_max


        