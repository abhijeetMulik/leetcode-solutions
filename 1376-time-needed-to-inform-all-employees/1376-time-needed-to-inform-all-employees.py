class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        dic = defaultdict(list)
        for i in range(n):
            dic[manager[i]].append(i)

        q  = deque([(headID, 0)]) # id, time
        ans = 0
        while q:
            i, time = q.popleft()
            ans = max(ans, time)
            for emp in dic[i]:
                q.append((emp, time + informTime[i]))
        return ans

