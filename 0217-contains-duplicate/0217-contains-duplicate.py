class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        if len(count) < len(nums):
            return True
        else:
            False
