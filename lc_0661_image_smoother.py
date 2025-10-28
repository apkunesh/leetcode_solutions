from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        deltas = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 0],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]
        copied_image = [elem.copy() for elem in img]
        for r in range(len(img)):
            for c in range(len(img[0])):
                local_sum, cells = 0, 0
                for delta in deltas:
                    nx, ny = r + delta[0], c + delta[1]
                    if nx < 0 or nx >= len(img) or ny < 0 or ny >= len(img[0]):
                        continue
                    local_sum += img[nx][ny]
                    cells += 1
                copied_image[r][c] = local_sum // cells
        return copied_image


soln = Solution().imageSmoother
print(f"{soln([[1,1,1],[1,0,1],[1,1,1]])} should be all 0s")
print(
    f"{soln( [[100,200,100],[200,50,200],[100,200,100]])} should be [[137,141,137],[141,138,141],[137,141,137]] "
)
