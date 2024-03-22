class Solution:    
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0,0                #         Follow up O(1)
        for i in nums:
            if count == 0:
                result = i
            if i != result :
                count-=1
            else:
                count+=1
        return result
        
        
        
        # count = Counter(nums)
        # cntMax = max(count.values())
        # for k, v in count.items():
        #     if v == cntMax:
        #         return k
        

    

                
        
        
        