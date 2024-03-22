class Solution:    
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        cntMax = max(count.values())
        for k, v in count.items():
            if v == cntMax:
                return k
                
        
        
        