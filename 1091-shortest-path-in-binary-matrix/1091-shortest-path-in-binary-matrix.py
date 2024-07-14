class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        q = deque([(0, 0, 1)]) #r, c, s
        n = len(grid)
        seen = {(0,0)}
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        def valid(r, c):
            return 0 <= r < n and 0 <= c < n and grid[r][c] == 0

        while q:
            r, c, s = q.popleft()
            if (r, c) == (n-1, n-1):
                return s
            
            for x, y in directions:
                new_r, new_c = r + y, c + x
                if valid(new_r, new_c) and (new_r, new_c) not in seen:
                    seen.add((new_r, new_c))
                    q.append((new_r, new_c, s + 1))
            
        return -1

