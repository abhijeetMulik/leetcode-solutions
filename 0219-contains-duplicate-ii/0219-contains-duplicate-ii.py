class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(int)
        for ka, v in enumerate(nums):
            if (v in dic) and (ka - dic[v] <= k):
                return True
                    
            dic[v] = ka
        return False