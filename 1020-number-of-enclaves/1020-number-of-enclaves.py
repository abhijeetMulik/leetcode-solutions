class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        seen = set()
        totalLand, edgeLand = 0, 0
        m = len(grid)
        n = len(grid[0])

        def ifEdge(row, col):
            return row in [0, m - 1] or col in [0, n - 1]

        def isNotValid(row, col):
            return  row < 0 or row == m or col < 0 or col == n or grid[row][col] == 0
        
        def dfs(r, c):
            if isNotValid(r, c) or (r, c) in seen:
                return 0
            ans = 1
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            seen.add((r, c))
            for x, y in directions:
                ans += dfs(r + x, c + y)
            return ans


        for r in range(m):
            for c in range(n):
                totalLand += grid[r][c]
                if grid[r][c] and (r, c) not in seen and ifEdge(r, c):
                    edgeLand += dfs(r, c)

        return totalLand - edgeLand

        