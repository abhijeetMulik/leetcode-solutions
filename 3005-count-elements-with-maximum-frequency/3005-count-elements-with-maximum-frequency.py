class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = Counter(nums)
        max_val = max(dic.values())
        count = 0
        for k in dic:
            if dic[k] == max_val:
                count += dic[k]
        return count
        