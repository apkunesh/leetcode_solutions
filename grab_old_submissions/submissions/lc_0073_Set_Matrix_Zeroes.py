class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        '''
        # Simple v1: O(n*m) time, go thru and identify all r,c with 0s, update all
        # associated rows + columns to 0. Takes O(n*m) time, O(n+m) space
        # In Amazon spirit, we'll do this version first.
        rows = set()
        cols = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        '''
        # V2 took some hints. It's basically about using the first row and column, itself
        # to denote whether the row/column should be cleared.
        first_row_blank = True if 0 in matrix[0] else False
        first_col_blank = True if 0 in [elem[0] for elem in matrix] else False
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if first_row_blank:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_col_blank:
            for i in range(len(matrix)):
                matrix[i][0] = 0