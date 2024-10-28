class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque([(0,0,k,0)]) #row, col, k, steps
        seen = {(0,0,k)} #row, col, k
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        while queue:
            row, col, remains, steps = queue.popleft()
            if row == m - 1 and col == n - 1:
                return steps
            
            for dx, dy in directions:
                new_row, new_col = dx + row, dy + col
                if valid(new_row, new_col):
                    if grid[new_row][new_col] == 0 and (new_row, new_col, remains) not in seen:
                            seen.add((new_row, new_col, remains))
                            queue.append((new_row, new_col, remains, steps + 1))
                    elif remains and (new_row, new_col, remains - 1) not in seen:
                        seen.add((new_row, new_col, remains - 1))
                        queue.append((new_row, new_col, remains - 1, steps + 1))
        
        return -1


        