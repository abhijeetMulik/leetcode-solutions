class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time, freshOranges = 0, 0
        m = len(grid)
        n = len(grid[0])
        q = deque() # r, c
        directions = [[0,1], [1,0], [-1,0], [0,-1]]
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    freshOranges += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        # print('q: ', q)
        # print('count :', freshOranges)
        def isValid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        while freshOranges > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for x, y in directions:
                    row, col = r + x, c + y
                    if isValid(row, col):
                        grid[row][col] = 2
                        freshOranges -= 1
                        # print('count :', freshOranges)
                        q.append((row, col))
            time += 1
            # print('time:', time)
            # print('q: ', q)
        # print('count :', freshOranges)
        if freshOranges == 0:
            return time
        else:
            return -1
