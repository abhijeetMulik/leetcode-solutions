class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        nums2 = set(nums[0])
        for i in range(1, len(nums)):
            nums2.intersection_update(set(nums[i]))

        return sorted(nums2)
        