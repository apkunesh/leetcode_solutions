class Solution:
    # NOTE: Idea was basically perfect! Set up a few mental test cases, which 
    # was a good idea. Made 2 typos, one of which was easily-diagnosed.

    # General idea: 2's represent the first elements we put in our queue
    # for BFS. We want to keep track of the # of times we move through the
    # queue (minutes) to reach all 1s, as well as the # of rotted fruits.
    # In the event that our queue is empty and the # of rotted fruits 
    # is not equal to the total number of fruits, we have failed to rot
    # all fruits, and we get -1.
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Mental test cases: single rotted fruit, no fruit, 1 rotted and 1 rottable,
        # 1 fruit no rot
        grid_size = len(grid) * len(grid[0])
        time_to_rot = 0
        num_fruits = 0 
        num_rotted = 0
        queue = deque()
        delta = [[-1,0],[1,0],[0,-1],[0,1]]
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    num_fruits +=1 # Rotted fruits at end should equal this.
                if grid[i][j] == 2:
                    queue.append((i,j))
                    seen.add((i,j))
                    num_rotted +=1
        while len(queue) > 0:
            if num_rotted == num_fruits:
                return time_to_rot
            time_to_rot += 1
            queue_size = len(queue)
            for i in range(queue_size):
                curr = queue.popleft()
                for dr,dc in delta:
                    nr,nc = curr[0]+dr,curr[1]+dc
                    # Exclusions
                    if nr<0 or nc<0 or nr>len(grid)-1 or nc> len(grid[0])-1:
                        continue
                    if grid[nr][nc]==0 or (nr,nc) in seen:
                        continue
                    queue.append((nr,nc))
                    seen.add((nr,nc))
                    num_rotted+=1
        if num_fruits == num_rotted:
            return time_to_rot
        return -1
        