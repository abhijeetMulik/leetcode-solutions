class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = defaultdict(int)
        for i in nums:
            if i in dic:
                return True
            dic[i] +=1
        return False