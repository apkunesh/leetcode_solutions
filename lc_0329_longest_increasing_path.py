"""
Given an m x n integers `matrix`, return the length of the longest increasing path in matrix.
From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap around is not allowed)
EX:
9 9 4
6 6 8
2 1 1
yields 4, corresponding to 1->2->6->9

3 4 5
3 2 6
2 2 1
yields 4, corresponding to 3->4->5->6

CONSTR:
m == matrix.length
n == matrix[i].length
1 <= m, n<= 200
0 <= matrix[i][j] <= 2^31 - 1
"""

"""
This is equivalent to the longest decreasing path. For each position, we'd like to know the longest increasing path from that point. Seems union-findy. Can't have multiple paths.
Naive choice would be to just do dfs from every single point.
Since strictly increasing, can just cache the result at that index and just ref the cache.
That should work.
"""

"""
Pseudocode:
dict taking tuple to maxlen

def recurse(i,j,val):
    OOB cases + nonincreasing case
    if i == len(matrix) or i == -1 or j == len(matrix[0]) or j == 1 or matrix[i][j]<=val:
        return 0
    if (i,j) in dict:
        return dict[(i,j)]
    Recursive case
    results = []
    for nx,ny in [[1,0],[0,1],[-1,0],[0,-1]]:
        results.append(recurse(i+nx,j+ny,matrix[i][j]))
    local_max = max(results)+1
    dict[(i,j)] = local_max
    return local_max

global_max = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        global_max = max(global_max,recurse(i,j,matrix[i][j]))
"""

from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        path_length_cache = {}

        def recurse(i, j, val):
            if (
                i == len(matrix)
                or i == -1
                or j == len(matrix[0])
                or j == -1
                or matrix[i][j] <= val
            ):
                return 0
            if (i, j) in path_length_cache:
                return path_length_cache[(i, j)]
            results = []
            for nx, ny in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
                results.append(recurse(i + nx, j + ny, matrix[i][j]))
            local_max = max(results) + 1
            path_length_cache[(i, j)] = local_max
            return local_max

        global_max = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                global_max = max(global_max, recurse(i, j, -2 * 10 ^ 31))
        return global_max
