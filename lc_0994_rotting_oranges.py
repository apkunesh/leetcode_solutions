from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot_count, orange_count, frontier, seen = 0, 0, deque(), set()
        neighbor_diffs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        n_steps = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rot_count += 1
                    orange_count += 1
                    frontier.append((i, j))
                    seen.add((i, j))
                elif grid[i][j] == 1:
                    orange_count += 1
        while frontier:
            for i in range(len(frontier)):
                rot_i, rot_j = frontier.popleft()
                for dx, dy in neighbor_diffs:
                    candidate = (rot_i + dx, rot_j + dy)
                    if (
                        candidate[0] >= len(grid)
                        or candidate[0] < 0
                        or candidate[1] < 0
                        or candidate[1] >= len(grid[0])
                    ):
                        continue
                    if candidate in seen:
                        continue
                    if grid[candidate[0]][candidate[1]] == 1:
                        rot_count += 1
                        frontier.append(candidate)
                    seen.add(candidate)
            n_steps += 1
        if rot_count == orange_count:
            return max([n_steps, 0])
        return -1
