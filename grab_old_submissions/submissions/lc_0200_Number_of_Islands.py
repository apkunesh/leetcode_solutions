
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs_discover_land(i,j,grid,discovered_land,visited):
            if i<0 or j<0 or i>len(grid)-1 or j>len(grid[0])-1 or grid[i][j] == '0':
                return discovered_land
            if (i,j) in discovered_land or (i,j) in visited:
                return discovered_land
            visited.append((i,j))
            discovered_land.add((i,j))
            discovered_land = dfs_discover_land(i+1,j,grid,discovered_land,visited)
            discovered_land = dfs_discover_land(i-1,j,grid,discovered_land,visited)
            discovered_land = dfs_discover_land(i,j-1,grid,discovered_land,visited)
            discovered_land = dfs_discover_land(i,j+1,grid,discovered_land,visited)
            visited.pop()
            return discovered_land
        n_islands = 0
        discovered_land = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                if (i,j) in discovered_land:
                    continue
                n_islands += 1
                new_discovered_land = dfs_discover_land(i,j,grid,discovered_land,[])
                discovered_land = discovered_land.union(new_discovered_land)
        return n_islands