class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"

        def dfs(row, col):
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if isValid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col)

        m = len(grid)
        n = len(grid[0])
        seen = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        ans = 0 

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in seen:
                    seen.add((row, col))
                    ans += 1
                    dfs(row, col)
        
        return ans

        