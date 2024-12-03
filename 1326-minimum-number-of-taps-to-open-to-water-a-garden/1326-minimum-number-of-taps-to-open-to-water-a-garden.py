class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        area = []
        for i in range(n + 1):
            area.append([i - ranges[i], i + ranges[i]])
        i, start, end = 0, 0, 0
        count = 0
        area.sort()
        print(area)

        for i in range(len(area)):
            while i < len(area) and area[i][0] <= start:
                end = max(end, area[i][1])
                i += 1
            count += 1
            start = end
            if end >= n:
                return count
            
        return count if end >= n else -1
            
        
