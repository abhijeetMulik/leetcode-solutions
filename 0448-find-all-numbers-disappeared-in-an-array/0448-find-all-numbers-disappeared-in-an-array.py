class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = set(nums)
        res = []
        for i in range(1, len(nums)+1):
            if i not in result:
                res.append(i)
        return res
        
