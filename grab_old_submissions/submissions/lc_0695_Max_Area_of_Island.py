class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Was a bit lazy with my checks: failed to return in the case that we were 
        # in water in the DFS. Consider just breaking these out initially ->
        # adding them together later.

        # Blaming alcohol slightly since I'm having a beer at Valley City, ND.
        rows, cols = len(grid),len(grid[0])
        max_area = 0
        known_land = set()

        def dfs_count_area(i,j,grid,area,known_land,visited):
            if i<0 or j<0 or i>len(grid)-1 or j> len(grid[0])-1 or (i,j) in known_land or (i,j) in visited or grid[i][j] == 0:
                return area, known_land
            known_land.add((i,j))
            visited.append((i,j))
            area+=1
            area,known_land = dfs_count_area(i+1,j,grid,area,known_land,visited)
            area,known_land = dfs_count_area(i-1,j,grid,area,known_land,visited)
            area,known_land = dfs_count_area(i,j+1,grid,area,known_land,visited)
            area,known_land = dfs_count_area(i,j-1,grid,area,known_land,visited)
            visited.pop()
            return area,known_land

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    continue
                island_area, _ = dfs_count_area(i,j,grid,0,known_land,[])
                if island_area > max_area:
                    max_area = island_area
        return max_area