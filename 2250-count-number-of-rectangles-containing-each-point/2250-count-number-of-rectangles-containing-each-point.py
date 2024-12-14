class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        limit = 101
        my_map = [[] for _ in range(limit)]

        for l, h in rectangles:
            my_map[h].append(l)
        
        for h in range(limit):
            my_map[h].sort()

        res = []
        for px, py in points:
            count = 0
            for h in range(py, limit):
                if len(my_map[h]) > 0:
                    index = bisect.bisect_left(my_map[h], px)
                    count += len(my_map[h]) - index
            res.append(count)
        
        return res


