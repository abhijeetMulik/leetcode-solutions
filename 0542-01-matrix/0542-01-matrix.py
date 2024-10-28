class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and mat[row][col] == 1

        queue = deque() # row, col, steps
        directions = [(1,0), (0,1), (-1,0), (0, -1)]
        seen = set()
        m = len(mat)
        n = len(mat[0])

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col, 0))
                    seen.add((row, col))

        while queue:
            row, col, steps = queue.popleft()        
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    # print(mat[new_row][new_col], ' : ', steps)
                    mat[new_row][new_col] = steps + 1
                    queue.append((new_row, new_col, steps + 1))

        return mat
        