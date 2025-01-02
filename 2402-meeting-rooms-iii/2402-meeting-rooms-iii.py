class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        ans = [0] * n
        meetings.sort()
        available = [i for i in range (n)] # room
        used = [] # endtime, room
        for start, end in meetings:
            
            # finish meeting
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)

            # make room available 
            if not available:
                endtime, room = heapq.heappop(used)
                end = endtime + (end - start)
                heapq.heappush(available, room)

            # add meeting
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))
            ans[room] += 1

        return ans.index(max(ans))
        