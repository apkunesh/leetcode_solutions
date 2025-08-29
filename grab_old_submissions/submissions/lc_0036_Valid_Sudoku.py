class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check 1: horizontal
        for i in range(len(board)):
            num_count = {q+1:1 for q in range(len(board[0]))}
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                if num_count[int(board[i][j])] == 0:
                    return False
                num_count[int(board[i][j])]-=1
        # check 2: vertical
        for i in range(len(board[0])):
            num_count = {q+1:1 for q in range(len(board))}
            for j in range(len(board)):
                if board[j][i] == '.':
                    continue
                if num_count[int(board[j][i])] == 0:
                    return False
                num_count[int(board[j][i])]-=1
        # check 3: sub-box
        top_lefts = [[0,0],[3,0],[6,0],[0,3],[3,3],[6,3],[0,6],[3,6],[6,6]]
        for i_top,j_top in top_lefts:
            num_count = {q+1:1 for q in range(len(board))}
            for i in range(i_top,i_top+3):
                for j in range(j_top,j_top+3):
                    if board[i][j] == '.':
                        continue
                    if num_count[int(board[i][j])] == 0:
                        return False
                    num_count[int(board[i][j])]-=1    
        return True