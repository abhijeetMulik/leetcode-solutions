class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def check(mid):
            count = 1
            prev = price[0]
            for p in range(1, len(price)):
                if price[p] >= prev + mid:
                    count += 1
                    prev = price[p]
            return count >= k
        
        price.sort()
        left = 1
        right = price[len(price) - 1] - price[0]
        ans = 0

        while left <= right:
            mid = left + (right - left ) // 2
            if check(mid):
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
        
        return ans
        