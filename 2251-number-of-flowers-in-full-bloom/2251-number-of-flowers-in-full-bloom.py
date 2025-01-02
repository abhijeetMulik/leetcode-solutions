class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        ans = [0] * len(people)
        people = [(p, i) for i, p in enumerate(people)]
        flowers.sort()
        end = []
        j = 0
        for p, i in sorted(people):
            while j < len(flowers) and flowers[j][0] <= p:
                heapq.heappush(end, flowers[j][1])
                j += 1
            
            while end and end[0] < p:
                heapq.heappop(end)
            
            ans[i] = len(end)
        
        return ans
        