class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def bfs(k):
            directions = [(-1,0), (0,-1), (0,1), (1,0)]
            seen = {(0,0)}
            q = deque([(0,0)])

            while q:
                row, col = q.popleft()
                if (row, col) == (m - 1, n - 1):
                    return True
                
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    if valid(new_row, new_col) and (new_row, new_col) not in seen:
                        if abs(heights[new_row][new_col] - heights[row][col]) <= k:
                            seen.add((new_row, new_col))
                            q.append((new_row, new_col))
            return False

        
        m = len(heights)
        n = len(heights[0])
        right = max(max(row) for row in heights)
        left = 0

        while left <= right:
            mid = (left + right) // 2
            if bfs(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left

