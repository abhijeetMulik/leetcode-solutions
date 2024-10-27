class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 0
        if grid[0][0] == 1:
            return -1
        
        m = n = len(grid)
        queue = deque([(0,0,1)]) #row, col, steps
        directions = [(0,1), (0,-1), (-1,-1), (-1,0), (-1,1), (1,-1), (1,0), (1,1)]
        seen = {(0,0)}

        while queue:
            row, col, steps = queue.popleft()
            if row == (n-1) and col == (n-1):
                return steps
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))
        

        return -1

        