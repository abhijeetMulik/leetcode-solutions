class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        left, total_sum, ans = 0, 0, 0
        q = deque()

        for n in range(len(chargeTimes)):
            while q and chargeTimes[q[-1]] < chargeTimes[n]:
                q.pop()
            q.append(n)

            total_sum += runningCosts[n]

            while q and chargeTimes[q[0]] + (n - left + 1) * total_sum > budget:
                if q[0] == left:
                    q.popleft()
                total_sum -= runningCosts[left]
                left += 1
            
            ans = max(ans, n - left + 1)
        return ans