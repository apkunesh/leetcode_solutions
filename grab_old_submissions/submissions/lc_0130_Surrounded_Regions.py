# Solution strategy: note that the only Os that survive contain members on the boundary. So, 
# if I grow a crystal of Os starting with Os on the edges, I have found all "live" groups.
# Once I have all live groups, I can just go over the rest of the board and call it X. Tada!
# I'll do this with BFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        # Establishing boundary
        to_examine = {(i,0) for i in range(rows)}
        to_examine.update({(i,cols-1) for i in range(rows)})
        to_examine.update({(0,j) for j in range(cols)})
        to_examine.update({(rows-1,j) for j in range(cols)})
        # Establishing Os on the boundary
        frontier = deque({elem for elem in to_examine if board[elem[0]][elem[1]] == "O"})
        live = set()
        neighbor_deltas = [[-1,0],[1,0],[0,-1],[0,1]]
        while frontier:
            r,c = frontier.popleft()
            if (r,c) in live:
                continue
            live.add((r,c))
            for dr,dc in neighbor_deltas:
                new_r, new_c = r+dr,c+dc
                if new_r < 0 or new_r > rows-1 or new_c < 0 or new_c > cols-1:
                    continue
                if board[new_r][new_c] == "O":
                    frontier.append((new_r,new_c))
        # All safe Os now live in live; let's go across and set everything to X.
        for i in range(rows):
            for j in range(cols):
                if (i,j) in live:
                    continue
                board[i][j] = "X"