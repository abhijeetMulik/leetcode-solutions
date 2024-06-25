class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = dict()

        for idx,val in enumerate(nums):
            noToFind = target - val
            if noToFind not in my_map:
                my_map[val] = idx
            else:
                return my_map[noToFind], idx