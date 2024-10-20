class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)
        heap = [(-ord(k), v) for k, v in count.items()]
        heapq.heapify(heap)
        ans = []
        while heap:
            k, v = heapq.heappop(heap)
            char = abs(k)
            times = min(v, repeatLimit)
            ans.append(chr(char) * times)
            v -= times

            if heap and v > 0:
                 k1, v1 = heapq.heappop(heap)
                 next_char = abs(k1)
                 ans.append(chr(next_char))
                 if v1 > 1:
                    heapq.heappush(heap, (k1, v1 - 1))
                 heapq.heappush(heap, (k, v))

        return "".join(ans)