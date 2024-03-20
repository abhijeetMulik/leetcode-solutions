class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap = {}
        for i in range(len(nums)):
            noToFind = target - nums[i]
            if nums[i] in mymap:
                return mymap[nums[i]], i
            else:
                mymap[noToFind] = i
        
        