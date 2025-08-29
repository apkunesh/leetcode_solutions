class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        prefix_sum = []
        for row in matrix:
            cur_prefix = [row[0]]
            for i in range(1,len(row)):
                cur_prefix.append(cur_prefix[i-1]+row[i])
            prefix_sum.append(cur_prefix)
        for i in range(1,len(matrix)):
            for j in range(len(matrix[0])):
                prefix_sum[i][j] = prefix_sum[i-1][j]+prefix_sum[i][j]
        self.double_sum = prefix_sum

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        base = self.double_sum[row2][col2]
        upper = self.double_sum[row1-1][col2] if row1>0 else 0
        left  = self.double_sum[row2][col1-1] if col1>0 else 0
        dc = self.double_sum[row1-1][col1-1] if (col1>0 and row1>0) else 0
        return base - upper - left + dc


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)