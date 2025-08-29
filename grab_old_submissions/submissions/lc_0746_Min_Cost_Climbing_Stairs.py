class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        second_last = 0
        last = 0
        for i in range(len(cost)):
            cur = min(last + cost[i],second_last+cost[i])
            second_last = last
            last = cur
        return last