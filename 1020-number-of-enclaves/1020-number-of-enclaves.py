class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        seen = set()
        edges, islands = 0, 0
        m = len(grid)
        n = len(grid[0])

        def isEdge(row, col):
            return row in [0, m - 1] or col in [0, n - 1]
        
        def isNotValid(row, col):
            return row < 0 or row >= m or col < 0  or col >= n or grid[row][col] == 0
        
        def dfs(row, col):
            if isNotValid(row,col) or (row,col) in seen:
                return 0
            ans = 1
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            seen.add((row, col))
            for dx, dy in directions:
                ans += dfs(row + dx, col + dy)
            return ans

        for row in range(m):
            for col in range(n):
                islands += grid[row][col]
                if grid[row][col] and (row,col) not in seen and isEdge(row,col):
                    edges += dfs(row,col)
        # print('islands :', islands)
        # print('edges: ', edges)
        return islands - edges
        