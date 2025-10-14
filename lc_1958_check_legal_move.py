from typing import List


class Solution:
    def checkMove(
        self, board: List[List[str]], rMove: int, cMove: int, color: str
    ) -> bool:
        # Idea: check the 8 directions for opposite colors ending in the same color.
        # Note that the first step must be the opposite color, the last step must the be same color, and blanks are automatically false.
        # If any gives a good line, we return true.
        opp_map = {"W": "B", "B": "W"}
        deltas = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        for delta in deltas:
            r, c = rMove + delta[0], cMove + delta[1]

            if (
                r < 0
                or r >= len(board)
                or c < 0
                or c >= len(board[0])
                or board[r][c] != opp_map[color]
            ):
                continue
            while (
                r >= 0
                and r < len(board)
                and c >= 0
                and c < len(board[0])
                and board[r][c] == opp_map[color]
            ):
                r = r + delta[0]
                c = c + delta[1]
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == color:
                return True
        return False


print(
    f'{Solution().checkMove([[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W")} should be false'
)

print(
    f'{Solution().checkMove(board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B")} should be True'
)
