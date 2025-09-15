from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # We'll do horizontal flips first
        rows, cols = len(grid), len(grid[0])
        if cols == 1:
            return rows
        for i in range(rows):
            if grid[i][0] == 0:
                for j in range(
                    1, cols
                ):  # Can skip the first col, as these will all be 1s
                    grid[i][j] = 0 if grid[i][j] == 1 else 1
        # Now we'll scan the columns and add up the score.
        score = 2 ** (cols - 1) * rows
        for j in range(1, cols):
            n_zeros = 0
            for i in range(rows):
                if grid[i][j] == 0:
                    n_zeros += 1
            max_ones = max([n_zeros, rows - n_zeros])
            score += max_ones * (2 ** (cols - 1 - j))
        return score
