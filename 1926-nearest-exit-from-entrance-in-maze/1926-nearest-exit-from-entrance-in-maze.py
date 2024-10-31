class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == "."

        def invalid(row, col):
            return row >= m or row < 0 or col >= n or col < 0

        m = len(maze)
        n = len(maze[0])
        # print('m',m,n)
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        queue = deque([(entrance[0], entrance[1], 0)]) #row, col, steps
        seen = {(entrance[0], entrance[1])} #row, col

        while queue:
            row, col, steps = queue.popleft()
            # print(row, col)
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))
                elif invalid(new_row, new_col) and steps > 0:
                    # print(new_row, new_col)
                    # print(seen)
                    return steps
        

        return -1



        


