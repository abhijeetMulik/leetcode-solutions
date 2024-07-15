class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == "."

        m = len(maze)
        n = len(maze[0])
        q = deque() 
        q.append([entrance[0], entrance[1], 0]) #row, col, steps
        # seen = set()
        # seen.add((entrance[0], entrance[1]))
        maze[entrance[0]][entrance[1]] = "+"
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        while q:
            row, col, steps = q.popleft()
            # print('exit condition :', row, ' ', col)
            
            for x, y in directions:
                next_r, next_c = row + y, col + x
                # print('next row and col: ', next_r, ' ', next_c)
                # print(valid(next_r, next_c))
                # print((next_r, next_c) not in seen)
                if valid(next_r, next_c):
                    if (next_r in [0, m - 1]  or next_c in [0, n - 1]) : # if this is exit
                        return steps + 1
                    # seen.add((next_r, next_c))
                    maze[next_r][next_c] = "+"
                    q.append([next_r, next_c, steps + 1])
                # print('queue: ', q)
                # print('seen: ', seen)

        return -1



        