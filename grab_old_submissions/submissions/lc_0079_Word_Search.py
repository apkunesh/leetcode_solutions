class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board,i,j,word,index,visited):
            if i > len(board)-1 or i <0 or j > len(board[0])-1 or j<0 or board[i][j] != word[index] or (i,j) in visited:
                return False
            if index == len(word)-1:
                return True
            visited.add((i,j))
            pairs = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            for row,col in pairs:
                neighbor_result = dfs(board,row,col,word,index+1,visited)
                if neighbor_result is True:
                    return True   
            visited.remove((i,j))         
            return False

        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                result = dfs(board,i,j,word,0,visited)
                if result is True:
                    return True
        return False
