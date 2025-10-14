from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # Idea: for each row and each column, there's a max height. For each i,j, we can build up to the min of the corresponding row and column.
        # So this should be O(n*m) regardless, and we'll do it in multiple passes to make my life simple.
        row_to_max_height = {i: 0 for i in range(len(grid))}
        col_to_max_height = {i: 0 for i in range(len(grid[0]))}
        for i in range(len(grid)):
            for j in range(len(grid)):
                row_to_max_height[i] = max(row_to_max_height[i], grid[i][j])
                col_to_max_height[j] = max(col_to_max_height[j], grid[i][j])
        print(col_to_max_height)
        grand_result = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                grand_result += (
                    min(row_to_max_height[i], col_to_max_height[j]) - grid[i][j]
                )
        return grand_result


soln = Solution().maxIncreaseKeepingSkyline
print(
    f"{soln(
 [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
)} should be 35"
)
print(f"{soln([[0,0,0],[0,0,0],[0,0,0]])} should be 0")

"""
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35

Input: grid = 6[0,0,0],[0,0,0],[0,0,0]]
Output: 0"""
