from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        """
        Idea: sort the costs. We'll have to buy the two most expensive ones, then we can get the next for free, and so on, until ultimately we have no more to buy.
        TC: O(nlogn) to sort, and O(n) to traverse.
        SC: Up to O(n) (timsort)
        """
        cost.sort(reverse=True)
        grand_sum = 0
        for i in range(len(cost)):
            if i % 3 == 2:
                continue
            grand_sum += cost[i]
        return grand_sum


print(Solution().minimumCost([1, 2, 3]) == 5)
print(Solution().minimumCost([6, 5, 7, 9, 2, 2]) == 23)
print(Solution().minimumCost([5, 5]) == 10)
