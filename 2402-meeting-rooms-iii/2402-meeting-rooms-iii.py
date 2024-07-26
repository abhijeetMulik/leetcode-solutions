class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        used = [] # end, room
        unused = [i for i in range(n)] # room
        ans = [0] * n

        for m in meetings:
            # end previous meeting
            while used and m[0] >= used[0][0]:
                e, r = heapq.heappop(used)
                heapq.heappush(unused, r)

            # handle delays
            if not unused:
                end, room = heapq.heappop(used)
                heapq.heappush(unused, room)
                m[1] = end + (m[1] - m[0])

            # schedule current meeting
            room = heapq.heappop(unused)
            heapq.heappush(used, (m[1], room))
            
            ans[room] += 1
        # print(ans)
        max_count = max(ans)
        return ans.index(max_count)
        