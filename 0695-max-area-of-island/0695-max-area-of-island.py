class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
        
        def dfs(row, col):
            seen.add((row, col))
            ans = 1
            for dx, dy in directions:
                r, c = row + dx, col + dy
                if isValid(r, c) and (r, c) not in seen:
                    ans += dfs(r, c)
            return ans

        m = len(grid)
        n = len(grid[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        seen = set()
        ans = 0

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in seen:
                    tmp = dfs(row, col)
                    ans = max(ans, tmp)

        return ans



        