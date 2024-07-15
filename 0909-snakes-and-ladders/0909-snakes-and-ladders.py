class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        q = deque([(1, 0)]) # square, moves
        seen = set()

        board.reverse()
        def pos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length - 1 - c       
            return r, c

        while q:
            square, moves = q.popleft()

            for i in range(0, 6):
                next_sq = square + (i + 1)
                r, c = pos(next_sq)
                if board[r][c] != -1:
                    next_sq = board[r][c]
                if next_sq == length * length:
                    return moves + 1
                if next_sq not in seen:
                    seen.add(next_sq)
                    q.append([next_sq, moves + 1])
        return -1
        