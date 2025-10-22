from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        ordered = []
        for i, cost in enumerate(costs):
            ordered.append((cost[1] - cost[0], i))  # B minus A
        ordered.sort()

        res = 0
        n = len(costs) // 2
        for i in range(n):
            res += costs[ordered[i][1]][1]
        for i in range(n, len(costs)):
            res += costs[ordered[i][1]][0]
        return res


soln = Solution().twoCitySchedCost

print(soln([[10, 20], [30, 200], [400, 50], [30, 20]]) == 110)
print(
    soln([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]])
    == 1859
)
print(
    soln(
        [
            [515, 563],
            [451, 713],
            [537, 709],
            [343, 819],
            [855, 779],
            [457, 60],
            [650, 359],
            [631, 42],
        ]
    )
    == 3086
)
