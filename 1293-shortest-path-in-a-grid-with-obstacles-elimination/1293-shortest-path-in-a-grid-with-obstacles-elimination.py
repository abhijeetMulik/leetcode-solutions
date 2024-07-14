class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        q = deque([(0,0,k,0)])
        seen = {(0,0,k)}
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while q:
            row, col, remains, steps = q.popleft()
            if row == m - 1 and col == n - 1:
                return steps
            
            for x, y in directions:
                new_r, new_c = row + y, col + x
                if valid(new_r, new_c):
                    if grid[new_r][new_c] == 0:
                        if (new_r, new_c, remains) not in seen:
                            seen.add((new_r, new_c, remains))
                            q.append((new_r, new_c, remains, steps + 1))
                    elif remains and (new_r, new_c, remains - 1) not in seen:
                        seen.add((new_r, new_c, remains - 1))
                        q.append((new_r, new_c, remains - 1, steps + 1))
        return -1

        