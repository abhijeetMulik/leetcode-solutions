class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = []
        for i in range(n + 1):
            taps.append([i - ranges[i], i + ranges[i]])
        # print(taps)
        start = 0
        end = 0
        count = 0
        while start < n:
            for t in taps:
                if start >= t[0]:
                    end = max(end, t[1])
            if start == end:
                return -1
            start = end
            count += 1

        return count

        