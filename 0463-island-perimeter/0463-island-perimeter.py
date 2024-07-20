class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        perimeter = 0
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    for x, y in directions:
                        new_r, new_col = r + y, c + x
                        if 0 <= new_r < n and 0 <= new_col < m:
                            if grid[new_r][new_col] == 0:
                                perimeter += 1
                        else:
                            perimeter += 1
        return perimeter



        