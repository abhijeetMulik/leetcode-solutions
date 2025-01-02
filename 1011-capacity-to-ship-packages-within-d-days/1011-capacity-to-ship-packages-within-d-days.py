class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(mid):
            total, ship = 0, 0
            for w in weights:
                if total + w > mid:
                    ship += 1
                    total = 0
                total += w
            # print('mid: ', mid, ' ship: ', ship)
            return ship + 1

        left = max(weights)
        right = sum(weights)
        ans = float('inf')
        while left <= right:
            mid = (left + right) // 2
            ship = check(mid)
            if ship <= days :
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
            # print('left: ', left, ' right :', right, ' ship: ', ship)
            # print('ans: ', ans)
        return ans
        