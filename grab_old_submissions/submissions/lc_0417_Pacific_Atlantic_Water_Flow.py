# General Idea (rd 3):
# Okay, the basic problem, I think, had to do with path tracking + the fact the "no path" case 
# was sometimes wrong when cells were of equal height.
# Instead, what we'll do is start with the ocean cells and attempt to build accessible neighbors out
# Sort of like turning gravity "upside down" and seeing which cells we actually hit.
# We'll do this with BFS, and we'll do it for both the pacific and atlantic sides.
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def can_reach(is_pacific):
            rows,cols = len(heights),len(heights[0])
            frontier = [(0,i) for i in range(cols)] + [(i,0) for i in range(rows)] if is_pacific else [(rows-1,i) for i in range(cols)] + [(i,cols-1) for i in range(rows)]
            frontier = deque(frontier)
            neighbor_deltas = [[-1,0],[1,0],[0,-1],[0,1]]
            seen = set()
            while frontier:
                r,c = frontier.popleft()
                if (r,c) in seen:
                    continue
                seen.add((r,c))
                for dr, dc in neighbor_deltas:
                    r_new,c_new = r+dr,c+dc
                    if r_new<0 or c_new<0 or r_new>=rows or c_new >= cols:
                        continue
                    if heights[r_new][c_new] >= heights[r][c]:
                        frontier.append((r_new,c_new))
            return seen
        pacific = can_reach(True)
        atlantic = can_reach(False)
        return [[elem[0],elem[1]] for elem in pacific if elem in atlantic]
