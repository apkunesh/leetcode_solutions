from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        first_row = [0] * len(matrix)
        result = []
        for _ in range(len(matrix[0])):
            result.append(first_row.copy())
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                result[j][i] = matrix[i][j]
        return result
