class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = deque()
        seen = set()
        m = len(mat)
        n = len(mat[0])
        directions = [(-1,0), (0,-1), (0,1), (1,0)]

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and mat[row][col] == 1

        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    q.append((row, col, 1))
                    seen.add((row, col))
        
        while q:
            row, col, steps = q.popleft()

            for x, y in directions:
                new_r, new_c = row + y, col + x
                if (new_r, new_c) not in seen and valid(new_r, new_c):
                    q.append((new_r, new_c, steps + 1))
                    seen.add((new_r, new_c))
                    mat[new_r][new_c] = steps

        return mat


        