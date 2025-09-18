from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # Idea: use points 1, 2 to establish a formula for a line; return whether the third point is on that line.
        if points[0] == points[1] or points[1] == points[2] or points[2] == points[0]:
            return False
        # Edge case: two lines fall on the same verical.
        all_xs = (points[0][0], points[1][0], points[2][0])
        if all_xs[0] == all_xs[1] or all_xs[1] == all_xs[2] or all_xs[0] == all_xs[2]:
            if all_xs[0] == all_xs[1] and all_xs[1] == all_xs[2]:
                return False
            return True
        # Edge case:
        m = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
        b = points[1][1] - m * points[1][0]
        # We include a tiny little epsilon to get around issues with floats
        eps = 2 * 10**-7
        return (
            points[2][1] > m * points[2][0] + b + eps
            or points[2][1] < m * points[2][0] + b - eps
        )


"""
Example 1:

Input: points = [[1,1],[2,3],[3,2]]
Output: true

Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: false
"""

print(Solution().isBoomerang([[1, 1], [2, 3], [3, 2]]) == True)
print(Solution().isBoomerang([[1, 1], [2, 2], [3, 3]]) == False)
