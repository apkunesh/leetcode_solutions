
from typing import List

class Solution:
    def longestIncreasingPath(self,matrix:List[List[int]]) -> int:
        path_length_cache = {}
        
        def recurse(i,j,val):
            if i ==len(matrix) or i==-1 or j==len(matrix[0]) or j==-1 or matrix[i][j]<=val:
                return 0
            if (i,j) in path_length_cache:
                return path_length_cache[(i,j)]
            results = []
            for nx,ny in [[1,0],[0,1],[0,-1],[-1,0]]:
                results.append(recurse(i+nx,j+ny,matrix[i][j]))
            local_max = max(results)+1
            path_length_cache[(i,j)] = local_max
            return local_max

        global_max = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                global_max = max(global_max,recurse(i,j,-2*10^31))
        return global_max