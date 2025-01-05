class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(mid):
            total = 0
            for c in candies:
                total += (c // mid)
            # print('mid: ', mid, ' total :', total)
            return total
        
        if sum(candies) < k:
            return 0
        
        left = 1
        right = max(candies)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            res = check(mid)
            if res >= k:
                left = mid + 1
                ans = max(ans, mid)
                # print('ans : ', ans)
            else:
                right = mid - 1
                
        return ans
        