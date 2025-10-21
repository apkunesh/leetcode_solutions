from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        """
        Idea: keep track of a "seen" set, which is gonna include all points inside the lattice.
        For each circle, carve out a square of points and, for each, consider (1) where in seen and (2) whether inside the circle. If new and inside, add to seen.
        Then return the length of this list
        TC can be *really* large, like O(c*n**2) where c is the number of circles and n is the size of the grid. This isn't *horrible* in that c is around 200 and n is also around 200 -> 200**3 -> 8M.
        """
        seen = set()
        for circle in circles:
            x_0 = circle[0]
            y_0 = circle[1]
            rad = circle[2]
            l = x_0 - rad
            r = x_0 + rad
            t = y_0 + rad
            b = y_0 - rad
            for x in range(l, r + 1):
                for y in range(b, t + 1):
                    if (x, y) in seen:
                        continue
                    if (x - x_0) ** 2 + (y - y_0) ** 2 > rad**2:
                        continue
                    seen.add((x, y))
        return len(seen)


print(Solution().countLatticePoints([[2, 2, 2], [3, 4, 1]]))  # 16
