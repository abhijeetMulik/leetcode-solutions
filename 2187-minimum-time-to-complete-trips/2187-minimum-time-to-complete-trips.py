class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(mid):
            res = 0
            for t in time:
                res += (mid // t)
            return res >= totalTrips            
        
        left = 1
        right = min(time) * totalTrips

        while left < right:
            mid = (left + right) // 2
            if  not check(mid):
                left = mid + 1
            else:
                right = mid
        
        return left