class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(m):
            total = 0
            count = 0
            for n in nums:
                if total + n <= m:
                    total += n
                else:
                    total = n
                    count += 1
            return count + 1 <= k
        
        res = 0
        left = max(nums)
        right = sum(nums) 

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
                res = mid
            else:
                left =  mid + 1
        
        return res
        