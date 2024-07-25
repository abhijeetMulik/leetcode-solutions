class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        cost = 0
        start = 0
        end = len(costs) - 1
        left = []
        right = []
        while k > 0:
            while len(left) < candidates and start <= end:
                heapq.heappush(left, costs[start])
                start += 1
            while len(right) < candidates and start <= end:
                heapq.heappush(right, costs[end])
                end -= 1
            
            top_left = left[0] if left else float('inf')
            top_right = right[0] if right else float('inf')
            
            if top_left <= top_right:
                cost += heapq.heappop(left)
            else:
                cost += heapq.heappop(right)
            k -= 1
        return cost

        