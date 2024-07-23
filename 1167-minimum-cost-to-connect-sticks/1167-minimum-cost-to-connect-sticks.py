class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        n = len(sticks)
        if n == 1:
            return 0
        ans = 0
        heapq.heapify(sticks)
        for i in range(n):
            # print(i ,' : ',sticks)
            first = heapq.heappop(sticks)
            # print('first:', first)
            second = heapq.heappop(sticks)
            # print('second:', second)
            heapq.heappush(sticks, (first + second))
            ans += first + second
            # print('length after add is: ', len(sticks))
            print(ans)
            if len(sticks) == 1:
                # last = heapq.heappop(sticks)
                # ans.append(heapq.heappop(sticks))
                # print('final ans:', ans)
                return ans
        return 0
    
                